from Builtin_helpers import Builtin_helpers
from Block_handler import Block_handler
from Function import Function
from Constant import Constant
from config import outputs

# handles defines
class Define:

  @staticmethod  
  def is_header(code_block):
    pass

  # must check beforehand whether the code block is a valid header
  # returns (name, parameters)
  @staticmethod  
  def get_header_name_parameters(header):
    trimmed_header = header[1: len(header) - 1]
    name_parameters = trimmed_header.split(' ')
    name = name_parameters[0]
    parameters = name_parameters[1:]
    return (name, parameters)

  @staticmethod
  def is_valid_parameters(parameters):
    return len(parameters) > 0
    
  # returns (is_valid, is_function, is_constant, name, parameters, body, value)
  @staticmethod  
  def is_define_is_valid_is_function_is_constant_name_parameters_body_value(code_block, functions, constants):
    
    # possible cases:
    # case 0: not a definition
    # case 1: valid function with one block (header)
    # case 1: invalid function with one block (header)
    # case 1: valid function with two blocks (header, body)
    # case 1: invalid function with two blocks (header, body)
    # case 5: valid constant with no block
    # case 6: invalid constant with no block
    # case 7: valid constant with one block (body)
    # case 8: invalid constant with one block (body)
    # case 9: invalid define (no valid operator or no valid body)
    
    trimmed_code_block = code_block[1: len(code_block) - 1]
    status_blocks = Block_handler.get_blocks(trimmed_code_block)
    status = status_blocks[0]
    blocks = status_blocks[1]

    if status:
      return (True, False, False, False, None, None, None, None)

    # not a define
    if 'define' not in code_block:
      return (False, False, False, False, None, None, None, None)
      
    # define at top level
    if trimmed_code_block.split(' ')[0] != 'define':
      outputs.append('define: found a definition that is not at the top level')
      return (True, False, False, False, None, None, None, None)
      
    # valid or invalid constant with no body
    if len(blocks) == 0:
      define_name_value = trimmed_code_block.split(' ')
      
      # missing components
      # be more specific
      if len(define_name_value) < 2:
        outputs.append('define: expected a variable name, or a function name and its variables (in parentheses), but nothing\'s there')
        return (True, False, False, False, None, None, None, None)
      elif len(define_name_value) < 3:
        name = define_name_value[1]
        outputs.append('define: expected an expression after the variable name {}, but nothing\'s there'.format(name))
        return (True, False, False, True, name, None, None, None)
      elif len(define_name_value) > 3:
        name = define_name_value[1]
        outputs.append('define: expected only one expression after the variable name {}, but found {} extra part'.format(name, len(define_name_value) - 3))        
      
      name = define_name_value[1]
      value = define_name_value[2]
      is_custom_name = Builtin_helpers.is_custom_name(name)
      is_valid_value = Builtin_helpers.is_valid_value(value)
      custom_names = list(functions.keys()) + list(constants.keys())
      is_custom_value = value in custom_names
      return (True, is_custom_name and (is_valid_value or is_custom_value), False, True, name, None, value, value)
    # valid or invalid function with header and no body
    # valid or invalid constant with body
    elif len(blocks) == 1:
      is_function_header_no_body = trimmed_code_block.split(' ')[1][0] == '('
      
      # function
      if is_function_header_no_body:
        # valid name and parameters for header
        name_parameters = Define.get_header_name_parameters(blocks[0][0])
        name = name_parameters[0]
        parameters = name_parameters[1]
        is_custom_name = Builtin_helpers.is_custom_name(name)
        is_valid_parameters = Define.is_valid_parameters(parameters)

        # valid non-block body
        header_left_idx = blocks[0][1]
        header_right_idx = blocks[0][2]
        non_block_code_block = code_block[:header_left_idx] + code_block[header_right_idx + 1:]
        trimmed_non_block_code_block = non_block_code_block[1: len(non_block_code_block) - 1]
        define_non_block_body = trimmed_non_block_code_block.split(' ')

        if len(define_non_block_body) > 2:
          return (True, False, True, False, name, parameters, None, None)

        non_block_body = define_non_block_body[1]
        is_valid_non_block_body = Builtin_helpers.is_valid_value(non_block_body)

        if not is_valid_non_block_body:
          return (True, False, True, False, name, parameters, None, None)

        return (True, True, True, False, name, parameters, non_block_body, None)
          
      # constant
      else:
        body_left_idx = blocks[0][1]
        body_right_idx = blocks[0][2]
        non_block_code_block = code_block[:body_left_idx] + code_block[body_right_idx + 1:]
        trimmed_non_block_code_block = non_block_code_block[1: len(non_block_code_block) - 1]
        define_name = trimmed_non_block_code_block.split(' ')

        if len(define_name) > 2:
          return (True, False, False, True, None, None, blocks[0][0], None)

        return (True, True, False, True, define_name[1], None, blocks[0][0], None)
        
    # valid or invalid function with header and body
    else:
      # valid name and parameters for header
      name_parameters = Define.get_header_name_parameters(blocks[0][0])
      name = name_parameters[0]
      parameters = name_parameters[1]
      is_custom_name = Builtin_helpers.is_custom_name(name)
      is_valid_parameters = Define.is_valid_parameters(parameters)

      # any non-block parts
      header_left_idx = blocks[0][1]
      header_right_idx = blocks[0][2]
      body_left_idx = blocks[1][1]
      body_right_idx = blocks[1][2]
      non_block_code_block = code_block[:header_left_idx] + code_block[header_right_idx + 1: body_left_idx] + code_block[body_right_idx + 1:]
      trimmed_non_block_code_block = non_block_code_block[1: len(non_block_code_block) - 1]
      define_non_block_parts = trimmed_non_block_code_block.split(' ')
      
      if len(define_non_block_parts) > 1:
        outputs.append('define: expected only one expression for the function body, but found {} extra part'.format(len(define_non_block_parts) - 1))
        return (True, False, True, False, name, parameters, blocks[1][0], None)
      
      return (True, is_custom_name and is_valid_parameters, True, False, name, parameters, blocks[1][0], None)

  # returns (status, functions, constants)
  @staticmethod  
  def get_function_constant(code_block, functions, constants):
    is_define_is_valid_is_function_is_constant_name_parameters_body_value = Define.is_define_is_valid_is_function_is_constant_name_parameters_body_value(code_block, functions, constants)
    is_define = is_define_is_valid_is_function_is_constant_name_parameters_body_value[0]
    is_valid = is_define_is_valid_is_function_is_constant_name_parameters_body_value[1]
    is_function = is_define_is_valid_is_function_is_constant_name_parameters_body_value[2]
    is_constant = is_define_is_valid_is_function_is_constant_name_parameters_body_value[3]
    name = is_define_is_valid_is_function_is_constant_name_parameters_body_value[4]
    parameters = is_define_is_valid_is_function_is_constant_name_parameters_body_value[5]
    body = is_define_is_valid_is_function_is_constant_name_parameters_body_value[6]
    value = is_define_is_valid_is_function_is_constant_name_parameters_body_value[7]
    
    # checks for duplicate define
    if name in functions or name in constants:
      outputs.append('{}: this name was defined previously and cannot be re-defined'.format(name))
      return True
    
    if is_define and not is_valid:
      outputs.append('a definition is used here before its definition')
      return True
    if is_function:
      function_inst = Function()
      function_inst.set_function(name, parameters, body)
      functions[name] = function_inst
      return False  
    elif is_constant:
      constant_inst = Constant()
      constant_inst.set_constant(name, body, value)
      constants[name] = constant_inst
      return False
    else:
      return False