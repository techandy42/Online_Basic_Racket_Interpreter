from Builtin_helpers import Builtin_helpers
from config import outputs

# handles functions
class Function:
  def __init__(self):
    self.name = ''
    self.parameters = []
    self.body = ''
    self.reached = False

  def set_function(self, name, parameters, body):
    self.name = name
    self.parameters = parameters
    self.body = body

  # returns (status, result)
  def match_functions(operator, values, functions):
    if operator in functions:
      if functions[operator].reached == True:
        if len(values) == len(functions[operator].parameters):
          modified_body = Function.get_modified_body(values, functions[operator].parameters, functions[operator].body)
          return (False, modified_body)
        else:
          outputs.append('{}: expects only {} arguments, but found {}'.format(operator, len(functions[operator].parameters), len(values)))
          return (True, None)
      else:
        outputs.append('{} is used here before its definition'.format(operator))
        return (True, None)
    else:
      return (False, None)

  def get_modified_body(values, parameters, body):
    body = body.replace('(', '( ').replace(')', ' )')
    parts = body.split(' ')
    for i in range(0, len(parameters)):
      for j in range(0, len(parts)):
        if parameters[i] == parts[j]:
          parts[j] = values[i]
    body = ' '.join(parts)
    body = body.replace('( ', '(').replace(' )', ')')
    return body

  def has_undefined_variables(self, functions, constants):
    non_brkt_parts = self.body.replace('(', '').replace(')', '').split(' ')
    names = Builtin_helpers.builtin_names + list(functions.keys()) + list(constants.keys())
    variables = []
    for i in range(0, len(non_brkt_parts)):
      if non_brkt_parts[i] not in names:
        if not Builtin_helpers.is_valid_value(non_brkt_parts[i]):
          variables.append(non_brkt_parts[i])

    if set(self.parameters) != set(variables):
      outputs.append('{}: this variable is not defined'.format(list(set(variables) - set(self.parameters))[0]))
      return True
    
    return False