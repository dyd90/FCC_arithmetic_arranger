ACCEPTABLE_OPERANDS = ['+', '-']
MAX_NUM_LEN = 4

def checked_no_error(problems):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  else:
    for expr in problems:
      split_str = expr.split(' ')
      operand_left = split_str[0]
      operator = split_str[1]
      operand_right = split_str[2]
      if operator not in ACCEPTABLE_OPERANDS:
        return "Error: Operator must be '+' or '-'."
      elif not(operand_left.isnumeric()) or not(operand_right.isnumeric()):
        return 'Error: Numbers must only contain digits.'
      elif len(operand_left) > MAX_NUM_LEN or len(operand_right) > MAX_NUM_LEN:
        return 'Error: Numbers cannot be more than four digits.'
      else:
        return 'True'


def arithmetic_arranger(problems, show_res=False):
  # check all the error cases
  check_err = checked_no_error(problems)
  
  # process solution if correct
  if check_err == 'True':
    # process solution

    # firstly need to loop over solution to get some bits of info

    # declare some vars
    num_problems = len(problems)
    operators = []
    total_spacing = []
    answer = []
    operand_lefts = []
    operand_rights = []

    for expr in problems:
      split_str = expr.split(' ')
      operand_left = split_str[0]
      operator = split_str[1]
      operand_right = split_str[2]
      
      operators.append(operator)
      operand_lefts.append(operand_left)
      operand_rights.append(operand_right)
      total_spacing.append(max(len(operand_left), len(operand_right))+2)
      answer.append(str((int(operand_left) + int(operand_right) if operator == '+' else int(operand_left) - int(operand_right))))

    arranged_problems = ""
    # time to print answer

    #first line
    for i in range(num_problems):
      arranged_problems += ' '*(total_spacing[i]-len(operand_lefts[i]))
      arranged_problems += operand_lefts[i]
      # print spaces
      if i < num_problems - 1:
        arranged_problems += '    '
    arranged_problems += '\n'

    #second line
    for i in range(num_problems):
      arranged_problems += operators[i]
      arranged_problems += ' '*(total_spacing[i]-len(operand_rights[i])-1)
      arranged_problems += operand_rights[i]
      # print spaces
      if i < num_problems - 1:
        arranged_problems += '    '
    arranged_problems += '\n'

    #third line
    for i in range(num_problems):
      arranged_problems += '-'*(total_spacing[i])
      # print spaces
      if i < num_problems - 1:
        arranged_problems += '    '

    # optional forth line
    if show_res:
      arranged_problems += '\n'
      for i in range(num_problems):
        arranged_problems += ' '*(total_spacing[i]-len(answer[i]))
        arranged_problems += answer[i]
        # print spaces
        if i < num_problems - 1:
          arranged_problems += '    '      
    return arranged_problems

  else:
    return check_err

