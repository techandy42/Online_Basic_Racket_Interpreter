from Builtin_helpers import Builtin_helpers
from Define import Define
from Function import Function
from Constant import Constant
from config import outputs

# executes a code block
class Execute_handler:

  # returns ()
  @staticmethod  
  def handle_code_block_types(code_block, results, functions, constants, show_steps):
    is_define_is_valid_is_function_is_constant_name_parameters_body_value = Define.is_define_is_valid_is_function_is_constant_name_parameters_body_value(code_block, functions, constants)
    is_function = is_define_is_valid_is_function_is_constant_name_parameters_body_value[2]
    is_constant = is_define_is_valid_is_function_is_constant_name_parameters_body_value[3]
    name = is_define_is_valid_is_function_is_constant_name_parameters_body_value[4]

    # referring to a single variable in constant definition
    reached_constants_names = []
    constants_names = list(constants.keys())
    for i in range(0, len(constants_names)):
      if constants[constants_names[i]].reached == True:
        reached_constants_names.append(constants_names[i])
    
    if is_function:
      functions[name].reached = True
    elif is_constant:
      constants[name].reached = True

      for i in range(0, len(reached_constants_names)):
        if reached_constants_names[i] == constants[name].body:
          constants[name].value = constants[reached_constants_names[i]].value
          return False
      
      if constants[name].value != None:
        return False
      result = Execute_handler.execute_code_block(constants[name].body, functions, constants, show_steps)
      if result == None:
        return True
      else:
        constants[name].value = result
        return False
    else:
      result = Execute_handler.execute_code_block(code_block, functions, constants, show_steps)
      results.append(result)
      if result == None:
        return True
      else:
        return False

  # evaluated whether a cond has a valid value that isn't null, and returns it
  # returns (status, is_finished_cond, result)
  @staticmethod
  def handle_cond(code_block):
    parts = code_block.replace('(', '( ').replace(')', ' )').split(' ')

    is_finished_cond = False
    has_cond = False 
    cond_valid_value = None
    left_idx = -1
    right_idx = -1
    left_brkt_number = 0
    right_brkt_number = 0
    # case 1: !has_cond
    # first cond that comes up becomes target cond
    # case 2: has_cond and has a valid cond_valid_value
    # returns the cond_valid_value
    # no new cond can take the spot
    # case 3: has_cond but no valid cond_valid_value
    # when hit left bracket after cond, reset has_cond, left_idx, left_brkt_number, right_brkt_number
    for i in range(0, len(parts)):
      if parts[i] == 'cond':
        if not has_cond:
          has_cond = True
          left_idx = i - 1
          left_brkt_number = 1
      elif parts[i] == '(':
        # handles hit left bracket after cond, without finding a valid value
        # resets
        if has_cond and cond_valid_value == None:
          has_cond = False
          left_idx = -1
          right_idx = -1
          left_brkt_number = 0
          right_brkt_number = 0
        elif has_cond:
          left_brkt_number += 1
      elif parts[i] == ')':
        if has_cond:
          right_brkt_number += 1
      elif Builtin_helpers.is_valid_value(parts[i]):
        if has_cond and cond_valid_value == None and parts[i] != 'null':
          cond_valid_value = parts[i]
      else:
        # handle invalid operator in non-block
        if has_cond and parts[i - 1] != '(':
          return (True, True, None)

      if has_cond and cond_valid_value != None and left_brkt_number == right_brkt_number and left_brkt_number != 0:
        is_finished_cond = True
        right_idx = i
        break
    
    if is_finished_cond:
      code_block = ' '.join(parts[: left_idx] + [cond_valid_value] + parts[right_idx + 1:]).replace('( ', '(').replace(' )', ')')
      return (False, True, code_block)
      
    return (False, False, None)
  
  # recursive method that executes the code_block until it is a numeric value
  @staticmethod  
  def execute_code_block(code_block, functions, constants, show_steps):
    if show_steps:
      outputs.append(code_block.replace(' null', ''))

    # handle cond
    status_is_finished_cond_result = Execute_handler.handle_cond(code_block)
    status = status_is_finished_cond_result[0]
    is_finished_cond = status_is_finished_cond_result[1]
    result = status_is_finished_cond_result[2]
    if status:
      outputs.append('cond: expected a clause with an answer or a question and an answer, but found something else')
      return None
    elif is_finished_cond:
      code_block = result
    
    # handle code block that has been evaluated
    if Builtin_helpers.is_valid_value(code_block):
      return code_block
    
    left_idx = -1
    right_idx = -1
    for i in range(0, len(code_block)):
      if code_block[i] == '(':
        left_idx = i
      elif code_block[i] == ')':
        right_idx = i
        
        code_subblock = code_block[left_idx: right_idx + 1] 
        left_code_subblock = code_block[:left_idx]
        right_code_subblock = code_block[right_idx + 1:]
        
        status_result = Execute_handler.call_functions(code_subblock, functions, constants, show_steps)
        status = status_result[0]
        result = status_result[1]
        
        if status:
          outputs.append('there has been an error running the code block between index {} and {}'.format(left_idx, right_idx))
          return None
        
        new_code_block = left_code_subblock + result + right_code_subblock
        return Execute_handler.execute_code_block(new_code_block, functions, constants, show_steps)
    
    outputs.append('unknown error has occured while running the code block between index {} and {}'.format(left_idx, right_idx))
    return None
  
  @staticmethod  
  def call_functions(code_subblock, functions, constants, show_steps):
    trimmed_code_subblock = code_subblock[1: len(code_subblock) - 1]
    operator_values = trimmed_code_subblock.split(' ')
    operator = operator_values[0]
    values = operator_values[1:]
    
    # convert symbolic parameters to builtin or custom constant values
    for i in range(0, len(values)):
      values[i] = Builtin_helpers.convert_builtin_constants(values[i])
      status_result = Constant.match_constants(values[i], constants)
      status = status_result[0]
      result = status_result[1]

      if status:
        return (True, None)
      values[i] = result

    calc_result = None
    
    # match operators to builtin helper functions 

    # generic helper functions
    if operator in Builtin_helpers.builtin_generic_helper_names:
      if operator == 'cond':
        calc_result = Builtin_helpers.cond(values)
        if calc_result == None:
          outputs.append('cond: all question results were false')
          return (True, None)
      elif operator == 'else' and len(values) == 1:
        calc_result = Builtin_helpers.else_keyword(values[0])
      elif operator == 'true' and len(values) == 1:
        calc_result = Builtin_helpers.true(values[0])
      elif operator == 'false' and len(values) == 1:
        calc_result = Builtin_helpers.false(values[0])
      elif operator == 'printf' and len(values) == 1:
        calc_result = Builtin_helpers.printf(values[0], show_steps)

    # numeric helper functions
    elif operator in Builtin_helpers.builtin_numeric_helper_names:
      for i in range(len(values)):
        if not Builtin_helpers.is_numeric_value(values[i]):
          outputs.append('{}: expects a number, given {}'.format(values[i]))
          return (True, None)

      # convert values to numeric values
      for i in range(0, len(values)):
        values[i] = Builtin_helpers.str_to_numeric(values[i])
      
      if operator == '=' and len(values) == 2:
        calc_result = Builtin_helpers.equal(values[0], values[1])
      elif operator == '<' and len(values) == 2:
        calc_result = Builtin_helpers.lt(values[0], values[1])
      elif operator == '>' and len(values) == 2:
        calc_result = Builtin_helpers.gt(values[0], values[1])
      elif operator == '<=' and len(values) == 2:
        calc_result = Builtin_helpers.lte(values[0], values[1])
      elif operator == '>=' and len(values) == 2:
        calc_result = Builtin_helpers.gte(values[0], values[1])
      elif operator == 'add1' and len(values) == 1:
        calc_result = Builtin_helpers.add1(values[0])
      elif operator == 'sub1' and len(values) == 1:
        calc_result = Builtin_helpers.sub1(values[0])
      elif operator == '+':
        calc_result = Builtin_helpers.add(values)
      elif operator == '-':
        calc_result = Builtin_helpers.sub(values)
      elif operator == '*':
        calc_result = Builtin_helpers.mul(values)
      elif operator == '/':
        calc_result = Builtin_helpers.div(values)
      elif operator == 'modulo' and len(values) == 2:
        calc_result = Builtin_helpers.modulo(values[0], values[1])
      elif operator == 'expt' and len(values) == 2:
        calc_result = Builtin_helpers.expt(values[0], values[1])
      elif operator == 'sqr' and len(values) == 1:
        calc_result = Builtin_helpers.sqr(values[0])
      elif operator == 'sqrt' and len(values) == 1:
        calc_result = Builtin_helpers.sqrt(values[0])
      elif operator == 'floor' and len(values) == 1:
        calc_result = Builtin_helpers.floor(values[0])
      elif operator == 'ceiling' and len(values) == 1:
        calc_result = Builtin_helpers.ceiling(values[0])
      elif operator == 'round' and len(values) == 1:
        calc_result = Builtin_helpers.round(values[0])
      elif operator == 'abs' and len(values) == 1:
        calc_result = Builtin_helpers.abs(values[0])
      elif operator == 'max':
        calc_result = Builtin_helpers.max(values)
      elif operator == 'min':
        calc_result = Builtin_helpers.min(values)
      elif operator == 'gcd' and len(values) == 2:
        calc_result = Builtin_helpers.gcd(values[0], values[1])
      elif operator == 'lcm' and len(values) == 2:
        calc_result = Builtin_helpers.lcm(values[0], values[1])
      elif operator == 'sin':
        calc_result = Builtin_helpers.sin(values)
      elif operator == 'cos':
        calc_result = Builtin_helpers.cos(values)
      elif operator == 'tan':
        calc_result = Builtin_helpers.tan(values)
      elif operator == 'log':
        calc_result = Builtin_helpers.log(values)
  
    # match operators to custom functions
    else:
      for i in range(0, len(values)):
        values[i] = str(values[i])
      status_result = Function.match_functions(operator, values, functions)
      status = status_result[0]
      result = status_result[1]

      if status:
        return (True, None)
      calc_result = result
    
    if calc_result == None:
      outputs.append('msg: invalid function name or parameter numbers')
      return (True, None)
    
    return (False, str(calc_result))