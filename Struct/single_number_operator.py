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

    # Handling simple one operator and one number
    if len(list_value) == 2:
        return list_value
    
    # Handle simple case where the list has exactly 3 elements
    if len(list_value) == 3:
        return [list_value[1], list_value[0], list_value[2]]

    # Process operators according to their precedence
    list_value = process_operators(list_value, ['^', 'pow'])  # Highest priority operators
    list_value = process_operators(list_value, ['*', '/', '%', 'mul', 'div', 'mod'])  # Level one operators
    list_value = process_operators(list_value, ['+', '-', 'add', 'sub'])  # Level two operators

    # If the list still has more than 3 elements, continue structuring it
    while len(list_value) > 3:
        sub_struct = [list_value[1], list_value[0], list_value[2]]
        list_value = [sub_struct] + list_value[3:]

    # Handle the case again if the list has exactly 3 elements after processing
    if len(list_value) == 3:
        return [list_value[1], list_value[0], list_value[2]]

    # Return the final structured list
    return list_value[0]

# Test examples
print(struct(['-', 5]))
print(struct([3, '*', 2]))  # Output: ['*', 3, 2]
print(struct([1, '+', 2, 'mul', 3]))  # Output: ['+', 1, ['mul', 2, 3]]
print(struct([2, 'mod', 3, '-', 4, '/', 5.2]))  # Output: ['-', ['mod', 2, 3], ['/', 4, 5.2]]