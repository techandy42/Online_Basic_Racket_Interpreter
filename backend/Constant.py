from Builtin_helpers import Builtin_helpers
from config import outputs

# handles constants
class Constant:
  def __init__(self):
    self.name = ''
    self.body = ''
    self.value = None
    self.reached = False

  def set_constant(self, name, body, value):
    self.name = name
    self.body = body
    self.value = value
      
  # returns (status, result)
  @staticmethod   
  def match_constants(val, constants):
    if val in constants:
      if constants[val].reached == False:
        outputs.append('{} is used before its definition'.format(val))
        return (True, None)
      else:
        return (False, constants[val].value)
    elif not Builtin_helpers.is_valid_value(val):
      outputs.append('{}: this variable is not defined'.format(val))
      return (True, None)  
    return (False, val)

  def has_self_reference(self):
    non_brkt_parts = self.body.replace('(', '').replace(')', '').split(' ')
    if self.name in non_brkt_parts:
      outputs.append('{} is used here before its definition'.format(self.name))
      return True
    
    return False