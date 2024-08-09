# 2 - 3  ->  ['-', 2, 3]
# 1 - 2 + 3  ->  ['+', ['-', 1, 2], 3]
# 1 * 2 - 3  ->  ['-', ['*', 1, 2], 3]
# 2.3 + 3 / 4.2 - 2  ->  ['-', ['+', 2.3, ['/', 3, 4.2]], 2]

# Upgrade the eval function to support recursive structures as described above.

# Notes:
# call calc function when the structure is simple structure, operator with two numbers .
# call eval recursively if one of the arguments is another structure (list).

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
    # Base case: if structure is a simple list [op, num1, num2]
    if isinstance(structure, list) and len(structure) == 3:
        op, arg1, arg2 = structure
        # Recursively evaluate if arguments are lists
        if isinstance(arg1, list):
            arg1 = eval(arg1)
        if isinstance(arg2, list):
            arg2 = eval(arg2)
        # Perform the calculation for the current simple structure
        return calc(op, arg1, arg2)
    
    else:
        raise ValueError("Invalid structure")


print(eval(['+', ['-', 1, 2], 3]))             # 2
print(eval(['-', 1, ['+', 2, 3]]))             # -4
print(eval(['+', ['+', 2, ['*', 3, 4]], 5]))   # 19
print(eval(['/', 1, 2]))                       # 0.5
print(eval(['*', 2, ['+', 1, 2]]))             # 6