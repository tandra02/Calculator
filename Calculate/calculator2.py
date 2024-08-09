# Add to calc option to raise an exceptions when the above errors happen.
# The error messages should be in the following formats,
# calc('/', 3, 0)  ->  Division by zero
# calc('$', 3, 2)  ->  Invalid operator "$"
# calc('+', [], 3)  ->  Invalid number "[]"

def calc(operator, one_number, two_number):
    try: # Check if one_number is 'int' or 'float'
        one_number = float(one_number) if '.' in str(one_number) else int(one_number)
    except (ValueError, TypeError):
        raise Exception(f'Invalid number "{one_number}"')

    try: # Check if two_number is 'int' or 'float'
        two_number = float(two_number) if '.' in str(two_number) else int(two_number)
    except (ValueError, TypeError):
        raise Exception(f'Invalid number "{two_number}"')

    # Check if the operator is valid
    if operator not in ['+', '-', '*', '/', '%', '^', 'add', 'sub', 'mul', 'div', 'pow', 'mod']:
        raise Exception(f'Invalid operator "{operator}"')

    # Perform the calculation
    if operator in ['+', 'add']:
        return one_number + two_number
    elif operator in ['-', 'sub']:
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
    
print(calc('$', 2, 3)) # Invalid operator "$"
print(calc('/', 2, 0)) # Division by zero
print(calc('%', 3.5, 0)) # Division by zero
print(calc('*', [], 's')) # Invalid number "[]"
print(calc('??', 5.4, 'not_a_number')) # Invalid number "not_a_number"