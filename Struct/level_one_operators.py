# Currently struct only supports level two operators.
# Your task is to add support for level one operators for struct.
# Make sure the order of calculations is taking place!
# Examples:

# struct([3, '*', 2])  ->  ['*', 3, 2]
# struct([1, '+', 2, 'mul', 3])  ->  ['+', 1, ['mul', 2, 3]]
# struct([2, 'mod', 3, '-', 4, '/', 5.2])  ->  ['-', ['mod', 2, 3], ['/', 4, 5.2]]

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
        i = 1 # To check the first operator which will be at index 1
        # Making sure to not go out of bounds
        while i < len(lst) - 1:
            if lst[i] in operators:
                left, op, right = lst[i - 1], lst[i], lst[i + 1]
                lst = lst[:i - 1] + [[op, left, right]] + lst[i + 2:]
            else:
                i += 2 # Move to the next operator
        return lst

    # Process level one operators ('*', '/', '%')
    list_value = process_operators(list_value, ['*', '/', '%', 'mul', 'div', 'mod'])

    # Process level two operators ('+', '-')
    list_value = process_operators(list_value, ['+', '-', 'add', 'sub'])

    return list_value[0] # Return the final structured list

print(struct([3, '*', 2]))                       # Expected output: ['*', 3, 2]
print(struct([1, '+', 2, '*', 3]))               # Expected output: ['+', 1, ['*', 2, 3]]
print(struct([2, '%', 3, '-', 4, '/', 5.2]))     # Expected output: ['-', ['%', 2, 3], ['/', 4, 5.2]]
print(struct([1, 'add', 2, 'mod', 3, '-', 4]))   # Expected output: ['-', ['add', 1, ['mod', 2, 3]], 4]
print(struct([5, '-', 5, 'mul', 5, 'div', 5]))   # Expected output: ['-', 5, ['div', ['mul', 5, 5], 5]]