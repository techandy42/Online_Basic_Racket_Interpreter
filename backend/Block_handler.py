from config import outputs

# handles code blocking
class Block_handler:

  @staticmethod  
  def brkt_parser(input):
    return input.replace('[', '(').replace(']', ')')
    
  # removes \n and excess whitespaces
  @staticmethod
  def format_code_block(code_block):
    code_block = code_block.replace('\n', '')
    is_whitespace = False
    whitespace_removed_code_block = ''
    for i in range(0, len(code_block)):
      if code_block[i] == ' ' and is_whitespace:
        continue
      else:
        whitespace_removed_code_block += code_block[i]
      if code_block[i] == ' ':
        is_whitespace = True
      else:
        is_whitespace = False
    
    return whitespace_removed_code_block
  
  # get code blocks and its end-point indexes
  # returns (status, blocks)
  @staticmethod
  def get_blocks(input):
    # store the starting index and ending index of the code blocks
    # (code_block, left_idx, right_idx)
    blocks = []
    
    # local variables
    left_idx = -1
    right_idx = -1
    err_right_idx = -1
    left_brkt_count = 0
    right_brkt_count = 0
  
    for i in range(0, len(input)):
      # handling stray right bracket error 
      if left_idx == -1 and right_idx == -1 and input[i] == ')':
        err_right_idx = i
      # handling left bracket
      if input[i] == '(':
        if left_idx == -1:
          left_idx = i
        left_brkt_count += 1
      # handling right bracket
      elif input[i] == ')' and left_idx != -1:
        right_idx = i
        right_brkt_count += 1
      # found a code block
      if left_brkt_count == right_brkt_count and left_idx != -1 and right_idx != -1:
        blocks.append((Block_handler.format_code_block(input[left_idx: right_idx + 1]), left_idx, right_idx + 1))
        left_idx = -1
        right_idx = -1
        left_brkt_count = 0
        right_brkt_count = 0
  
    lone_brkt_err_status = Block_handler.lone_brkt_err_handling(input, left_idx, right_idx, err_right_idx)
  
    mult_brkt_err_status = Block_handler.mult_brkt_err_handling(blocks)
    
    return (lone_brkt_err_status or mult_brkt_err_status, blocks)

  @staticmethod
  def get_err_left_idx(rev_input):
    left_brkt_count = 0
    right_brkt_count = 0
    for i in range(0, len(rev_input)):
      if left_brkt_count > right_brkt_count:
        return len(rev_input) - i
      if rev_input[i] == ')':
        right_brkt_count += 1
      elif rev_input[i] == '(':
        left_brkt_count += 1
    return -1

  # handling bracket syntax errors
  @staticmethod
  def lone_brkt_err_handling(input, left_idx, right_idx, err_right_idx):
    # right bracket error
    if err_right_idx != -1:
      outputs.append('read-syntax: unexpected ) at index {}'.format(err_right_idx))
      return True
    
    # left bracket error
    elif left_idx != -1:
      outputs.append('read-syntax: expected a ) to close ( at index {}'.format(Block_handler.get_err_left_idx(input[::-1])))
      return True 
  
    return False
  
  # multiple bracket error
  @staticmethod
  def mult_brkt_err_handling(blocks):
    for i in range(0, len(blocks)):
      code_block = blocks[i][0]
      trimmed_code_block = code_block[1: len(code_block) - 1]
      if trimmed_code_block[0] == '(' and trimmed_code_block[len(trimmed_code_block) - 1] == ')':
        outputs.append('read-syntax: multiple brackets found at index {} and {}'.format(blocks[i][1], blocks[i][2]))
        return True
    return False