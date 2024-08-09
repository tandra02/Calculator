# Create a function parse which gets string and returns a structured format.
# This time we are going to deal only with simple calculation, with one operator.
# Examples:

# parse('1+2')  ->  ['+', 1, 2]
# parse('  3*  5')  ->  ['*', 3, 5]
# parse('3 pow 2.5')  ->  ['pow', 3, 2.5]
# Make use of get_next and struct functions.


def calc(operator, one_number, two_number=None):
    try:  # Check if one_number is 'int' or 'float'
        one_number = float(one_number) if '.' in str(one_number) else int(one_number)
    except (ValueError, TypeError):
        raise Exception(f'Invalid number "{one_number}"')

    if two_number is not None:
        try:  # Check if two_number is 'int' or 'float'
            two_number = float(two_number) if '.' in str(two_number) else int(two_number)
        except (ValueError, TypeError):
            raise Exception(f'Invalid number "{two_number}"')

    # Check if the operator is valid
    if operator not in ['+', '-', '*', '/', '%', '^', 'add', 'sub', 'mul', 'div', 'pow', 'mod']:
        raise Exception(f'Invalid operator "{operator}"')

    # Perform the calculation
    if operator in ['+', 'add']:
        if two_number is None:
            return +one_number
        return one_number + two_number
    elif operator in ['-', 'sub']:
        if two_number is None:
            return -one_number
        return one_number - two_number
    elif operator in ['*', 'mul']:
        return one_number * two_number
    elif operator in ['/', 'div']:
        if two_number == 0:
            raise Exception("Division by zero")
        return one_number / two_number
    elif operator in ['%', 'mod']:
        if two_number == 0:
            raise Exception("Division by zero")
        return one_number % two_number
    elif operator in ['^', 'pow']:
        return one_number ** two_number
    else:
        raise Exception(f'Invalid operator "{operator}"')

def eval(structure):
    if not isinstance(structure, list):
        raise ValueError(f'Failed to evaluate "{structure}"')
    
    # Base case: if structure is a simple list [op, num1, num2]
    elif isinstance(structure, list) and len(structure) == 3:
        op, arg1, arg2 = structure
        # Recursively evaluate if arguments are lists
        if isinstance(arg1, list):
            arg1 = eval(arg1)
        if isinstance(arg2, list):
            arg2 = eval(arg2)
        # Perform the calculation for the current simple structure
        return calc(op, arg1, arg2)
    
    # For single number and operator
    elif len(structure) == 2:
        op, arg1 = structure
        # Recursively evaluate if arguments are lists
        if isinstance(arg1, list):
            arg1 = eval(arg1)
        return calc(op, arg1)
    
    # Exception Handling
    elif len(structure) == 1:
        raise ValueError(f'Failed to evaluate "{structure}"')
    elif len(structure) > 3:
        raise ValueError(f'Failed to evaluate "{structure}"')
    elif structure == "not a list":
        raise ValueError(f'Failed to evaluate "{structure}"')
    
    else:
        raise ValueError(f'Failed to evaluate "{structure}"')

def struct(list_value):
    def process_operators(lst, operators):
        i = 1  # Start at the first operator in the list
        while i < len(lst) - 1:  # Ensure we don't go out of bounds
            if lst[i] in operators:  # Check if the current element is in the operators list
                left, op, right = lst[i - 1], lst[i], lst[i + 1]  # Get the left value, operator, and right value
                lst = lst[:i - 1] + [[op, left, right]] + lst[i + 2:]  # Replace with the structured list
            else:
                i += 2  # Move to the next operator
        return lst

    if not isinstance(list_value, list):
        raise ValueError(f'Failed to structure "{list_value}"')

    if len(list_value) == 1:
        raise ValueError(f'Failed to structure "{list_value}"')

    if len(list_value) == 2:
        return list_value

    if len(list_value) == 3:
        if isinstance(list_value[0], (int, float)) and list_value[1] in ['+', '-', '*', '/', '%', '^', 'add', 'sub', 'mul', 'div', 'pow', 'mod'] and isinstance(list_value[2], (int, float)):
            return [list_value[1], list_value[0], list_value[2]]
        return [list_value[1], list_value[0], list_value[2]]

    if len(list_value) == 4:
        raise ValueError(f'Failed to structure "{list_value}"')
        
    if len(list_value) > 3:
        list_value = process_operators(list_value, ['^', 'pow'])  # Highest priority operators
        list_value = process_operators(list_value, ['*', '/', '%', 'mul', 'div', 'mod'])  # Level one operators
        list_value = process_operators(list_value, ['+', '-', 'add', 'sub'])  # Level two operators
        list_value = process_operators(list_value, ['t'])  # Typos
        
        if len(list_value) > 3:
            raise ValueError(f'Failed to structure "{list_value}"')

    if len(list_value) == 3:
        return [list_value[1], list_value[0], list_value[2]]

    raise ValueError(f'Failed to structure "{list_value}"')

def get_next(string_value, start_index):
    operators = {'+', '-', '*', '/', '%', '^', 'add', 'sub', 'mul', 'div', 'pow', 'mod'}
    num_str = ""
    i = start_index

    # Check if the string is empty
    if not string_value:
        raise ValueError("End of string")
    
    # Check if the start index is beyond the length of the string
    if start_index >= len(string_value):
        raise IndexError("End of string")
    
    # Check if the first character at start_index is part of a number
    if string_value[i].isdigit() or string_value[i] == '.':
        while i < len(string_value) and (string_value[i].isdigit() or string_value[i] == '.'):
            num_str += string_value[i]
            i += 1
        if '.' in num_str:
            return float(num_str)
        else:
            return int(num_str)
    
    # Check for multi-character operators or alphabetic strings
    elif string_value[i].isalpha():
        while i < len(string_value) and string_value[i].isalpha():
            num_str += string_value[i]
            i += 1
        if num_str in operators:
            return num_str
        else:
            return num_str
    
    # If no number or alphabetic string, return the single character
    else:
        return string_value[start_index]
    
def parse(user_created_string):
    # Remove all whitespaces from the string
    user_created_string = user_created_string.replace(' ', '')

    # Initialize the starting index
    start_index = 0

    # Get the first number or operator
    a1 = get_next(user_created_string, start_index)
    start_index += len(str(a1))

    # Get the operator
    a2 = get_next(user_created_string, start_index)
    start_index += len(str(a2))

    # Get the second number
    a3 = get_next(user_created_string, start_index)

    # Structure the parsed elements
    return struct([a1, a2, a3])

# Test the parse function
print(parse('1+2'))  # Expected output: ['+', 1, 2]
print(parse('  3*  5'))  # Expected output: ['*', 3, 5]
print(parse('3 pow 2.5'))  # Expected output: ['pow', 3, 2.5]
print(parse('2*(3+4)'))