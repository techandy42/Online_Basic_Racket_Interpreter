import math

from config import outputs

class Builtin_helpers:
  # builtin constants
  pi = 3.141592653589793
  e = 2.718281828459045

  builtin_names = ['cond', 'else', 'true', 'false', '=', '>', '<', '>= ', '<=', 'add1', 'sub1', '+', '-', '*', '/', '%', 'expt', 'sqr', 'sqrt', 'floor', 'ceiling', 'round', 'abs', 'max', 'min', 'gcd', 'lcm', 'sin', 'cos', 'tan', 'log', 'printf']
  builtin_generic_helper_names = ['cond', 'else', 'true', 'false', 'printf']
  builtin_numeric_helper_names = ['=', '>', '<', '>= ', '<=', 'add1', 'sub1', '+', '-', '*', '/', '%', 'expt', 'sqr', 'sqrt', 'floor', 'ceiling', 'round', 'abs', 'max', 'min', 'gcd', 'lcm', 'sin', 'cos', 'tan', 'log']
  
  @staticmethod  
  def is_valid_value(val):
    if val == 'null' or val == 'true' or val == 'false':
      return True
    if val[0] == '-':
      val = val[1:]
    return val.replace('.', '').isdigit()

  @staticmethod  
  def is_numeric_value(val):
    if val[0] == '-':
      val = val[1:]
    return val.replace('.', '').isdigit()

  @staticmethod  
  def is_custom_name(name):
    return name not in Builtin_helpers.builtin_names
  
  @staticmethod  
  def str_to_numeric(val):
    if val == 'null' or val == 'true' or val == 'false':
      return val
    if not Builtin_helpers.is_valid_value(val):
      return None

    if '.' in val:
      return float(val)
    else:
      return int(val)
  
  @staticmethod  
  def convert_builtin_constants(val):
    if val == 'pi':
      return str(Builtin_helpers.pi)
    elif val == 'e':
      return str(Builtin_helpers.e)
    else:
      return val

  # generic functions
  
  @staticmethod  
  def cond(values):
    for i in range(0, len(values)):
      if values[i] != 'null':
        return values[i]
    return None

  @staticmethod  
  def else_keyword(val):
    return val

  @staticmethod  
  def true(val):
    return val

  @staticmethod  
  def false(val):
    return 'null'

  @staticmethod  
  def printf(val, show_steps):
    if not show_steps:
      outputs.append('>>> {}'.format(val))
    return val

  # numeric functions
  
  @staticmethod  
  def equal(val1, val2):
    if val1 == val2:
      return 'true'
    else:
      return 'false'

  @staticmethod  
  def gt(val1, val2):
    if val1 > val2:
      return 'true'
    else:
      return 'false'

  @staticmethod  
  def lt(val1, val2):
    if val1 < val2:
      return 'true'
    else:
      return 'false'

  @staticmethod  
  def gte(val1, val2):
    if val1 >= val2:
      return 'true'
    else:
      return 'false'

  @staticmethod  
  def lte(val1, val2):
    if val1 <= val2:
      return 'true'
    else:
      return 'false'
  
  @staticmethod  
  def add1(val):
    return val + 1

  @staticmethod  
  def sub1(val):
    return val - 1
  
  @staticmethod  
  def add(values):
    result = 0
    for i in range(0, len(values)):
      result += values[i]
    return result

  @staticmethod  
  def sub(values):
    result = values[0]
    for i in range(1, len(values)):
      result -= values[i]
    return result

  @staticmethod 
  def mul(values):
    result = 1
    for i in range(0, len(values)):
      result *= values[i]
    return result

  @staticmethod  
  def div(values):
    result = values[0]
    for i in range(1, len(values)):
      result /= values[i]
    return result

  @staticmethod  
  def modulo(val1, val2):
    return val1 % val2

  @staticmethod  
  def expt(val1, val2):
    return val1 ** val2

  @staticmethod  
  def sqr(val):
    return val ** 2

  @staticmethod
  def sqrt(val):
    return val ** (1/2)

  @staticmethod  
  def floor(val):
    return math.floor(val)

  @staticmethod  
  def ceiling(val):
    return math.ceil(val)

  @staticmethod
  def round(val):
    return math.round(val)

  @staticmethod  
  def abs(val):
    return math.abs(val)
  
  @staticmethod  
  def max(values):
    return max(values)

  @staticmethod  
  def min(values):
    return min(values)

  @staticmethod  
  def gcd(val1, val2):
    return math.gcd(val1, val2)

  @staticmethod  
  def lcm(val1, val2):
    greater = -1
    lcm = -1
    if val1 > val2:
      greater = val1
    else:
      greater = val2
    while(True):
      if greater % val1 == 0 and greater % val2 == 0:
        lcm = greater
        break
      greater += 1
    return lcm

  @staticmethod
  def sin(val):
    return math.sin(val)

  @staticmethod
  def cos(val):
    return math.cos(val)

  @staticmethod
  def tan(val):
    return math.tan(val)

  @staticmethod
  def log(val):
    return math.log(val)