# Create the function struct which gets list in the above format and returns the format applicable to the eval function.
# Currently deal only with basic operators '+' and '-'.

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
    if len(list_value) == 3:
        return [list_value[1], list_value[0], list_value[2]]

    while len(list_value) > 3:
        sub_struct = [list_value[1], list_value[0], list_value[2]]
        list_value = [sub_struct] + list_value[3:]

    if len(list_value) == 3:
        return [list_value[1], list_value[0], list_value[2]]
    return list_value


print(struct([4.5, '-', 3]))  # Expected output: ['-', 4.5, 3]
print(struct([4.5, '-', 3, '+', 2]))  # Expected output: ['+', ['-', 4.5, 3], 2]
print(struct([1, 'sub', 2, 'add', 3, '+', 4]))  # Expected output: ['+', ['add', ['sub', 1, 2], 3], 4]
print(struct([1, '+', 2, '+', 3, '+', 4]))     # Expected output: ['+', ['+', ['+', 1, 2], 3], 4]
print(struct([2, '%', 3, '-', 4, '/', 5.2]))