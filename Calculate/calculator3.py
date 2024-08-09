# Add support for single number operators for '+' and '-'.
# Add default value, None, to the 3rd argument of calc

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
    
print(calc('+', 4.4))      # 4.4
print(calc('-', 4.4))      # -4.4
print(calc('add', 4.4))    # 4.4
print(calc('sub', 4.4))    # -4.4
print(calc('+', 4, 5))     # 9
print(calc('-', 4, 5))     # -1
print(calc('*', 4, 5))     # 20
print(calc('/', 4, 5))     # 0.8
print(calc('%', 4, 5))     # 4
print(calc('^', 2, 3))     # 8