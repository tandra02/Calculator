# Add support for multiple operators in parse function.

def calc(op, n1, n2=None):
    if not isinstance(n1, int) and not isinstance(n1, float):
        raise Exception('Invalid number "' + str(n1) + '"')

    if n2 is None:
        if op == '+' or op == 'add':
            return n1
        if op == '-' or op == 'sub':
            return -n1

        raise Exception('Invalid operator "' + op + '"')

    if not isinstance(n2, int) and not isinstance(n2, float):
        raise Exception('Invalid number "' + str(n2) + '"')

    if op == '+' or op == 'add':
        return n1 + n2
    if op == '-' or op == 'sub':
        return n1 - n2
    if op == '*' or op == 'mul':
        return n1 * n2
    if op == '/' or op == 'div':
        if n2 == 0:
            raise Exception("Division by zero")
        return n1 / n2
    if op == '%' or op == 'mod':
        if n2 == 0:
            raise Exception("Division by zero")
        return n1 % n2
    if op == '^' or op == 'pow':
        return n1 ** n2

    raise Exception('Invalid operator "' + op + '"')


def eval(lst):
    if not isinstance(lst, list):
        raise Exception('Failed to evaluate "' + str(lst) + '"')
    if len(lst) == 2:
        op = lst[0]
        n = lst[1]
        if not isinstance(n, list):
            return calc(op, n)

        if isinstance(n, list):
            n = eval(n)

        return calc(op, n)
    elif len(lst) == 3:
        op = lst[0]
        n1 = lst[1]
        n2 = lst[2]
        if not isinstance(n1, list) and not isinstance(n2, list):
            return calc(op, n1, n2)
        
        if isinstance(n1, list):
            n1 = eval(n1)
        if isinstance(n2, list):
            n2 = eval(n2)

        return calc(op, n1, n2)
    else:
        raise Exception('Failed to evaluate "' + str(lst) + '"')


LEVEL_TWO_OPERATORS = ['+', '-', 'add', 'sub']
LEVEL_ONE_OPERATORS = ['*', '/', '%', 'mul', 'div', 'mod']
FUNCTIONS_OPERATORS = ['^', 'pow']
def struct(lst):
    if not isinstance(lst, list) or len(lst) <= 1:
        raise Exception('Failed to structure "' + str(lst) + '"')

    if len(lst) == 2:
        return lst

    lst_cpy = lst
    operators_groups = [FUNCTIONS_OPERATORS, LEVEL_ONE_OPERATORS, LEVEL_TWO_OPERATORS]
    for operators_group in operators_groups:
        i = 0
        while i < len(lst):
            if lst[i] in operators_group:
                if len(lst) - 1 == i:
                    raise Exception('Failed to structure "' + str(lst_cpy) + '"')
                if len(lst) == 3:
                    return [lst[i], lst[i - 1], lst[i + 1]]
                temp = lst[:i - 1]
                temp.append([lst[i], lst[i - 1], lst[i + 1]])
                temp += lst[i + 2:]
                lst = temp
            else:
                i += 1

    return lst


NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def get_next(s, i):
    if i >= len(s):
        raise Exception('End of string')
    res = ''
    if s[i] in NUMBERS or s[i] == '.':
        is_float = False
        while i < len(s) and (s[i] in NUMBERS or s[i] == '.'):
            res += s[i]
            if s[i] == '.':
                is_float = True
            i += 1

        if is_float:
            return float(res)
        return int(res)
    else:
        while i < len(s) and not (s[i] in NUMBERS or s[i] == '.'):
            res += s[i]
            i += 1

        return res


def parse(s):
    s = s.replace(' ', '')
    i = 0
    res = []
    while i < len(s):
        temp = get_next(s, i)
        res.append(temp)
        i += len(str(temp))
    return struct(res)



print(parse('1 + 2 - 3'))   # ['-', ['+', 1, 2], 3]
print(parse("5.4add3div1.2"))  # ['add', 5.4, ['div', 3, 1.2]]
print(parse("1+2* 3 - 6"))     # ['-', ['+', 1, ['*', 2, 3]], 6]
print(parse("1+2+3+4"))        # ['+', ['+', ['+', 1, 2], 3], 4]