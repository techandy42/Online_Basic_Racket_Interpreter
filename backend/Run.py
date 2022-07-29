from Block_handler import Block_handler
from Execute_handler import Execute_handler
from Define import Define
from config import outputs

class Run:
  def run(input, show_steps):
    
    try:
      for i in range(len(outputs)):
        outputs.pop()

      parsed_input = Block_handler.brkt_parser(input)
      status_blocks = Block_handler.get_blocks(parsed_input)
      status = status_blocks[0]
      blocks = status_blocks[1]
      
      # bracket syntax error
      if status:
        outputs.append('exiting program...')
        
        return False
    
      # initializing functions and constants
      functions = {}
      constants = {}
      for i in range(0, len(blocks)):
        # the functions and constants are not reached yet
        status = Define.get_function_constant(blocks[i][0], functions, constants)
        if status:
          outputs.append('exiting program...')
          
          return False
          
      # check for function undefined variables
      function_names = list(functions.keys())
      for i in range(0, len(function_names)):
        status = functions[function_names[i]].has_undefined_variables(functions, constants)
        if status:
          
          return False
          
      # check for self referencing constants
      constant_names = list(constants.keys())
      for i in range(0, len(constant_names)):
        status = constants[constant_names[i]].has_self_reference()
        if status:
          
          return False
      
      results = []
        
      # iterative through the blocks and execute them
      for i in range(0, len(blocks)):
        status = Execute_handler.handle_code_block_types(blocks[i][0], results, functions, constants, show_steps)
        if status:
          outputs.append('exiting program...')
          
          return False

      return True

    except Exception as e:
      outputs.append('some unexpected error occurred')
      outputs.append('exiting program...')

      return False
    