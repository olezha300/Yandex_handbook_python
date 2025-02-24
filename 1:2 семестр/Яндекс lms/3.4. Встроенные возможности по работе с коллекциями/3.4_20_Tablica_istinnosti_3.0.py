from itertools import product

OPERATORS = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

PRIORITY = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def postfix_expression(expression, variables):
    stack, result, lst = [], [], expression.split()
    for i in lst:
        if i in variables:
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result.append(OPERATORS[stack.pop()])
            stack.pop()
        elif i in OPERATORS.keys():
            while len(stack) and PRIORITY[i] >= PRIORITY[stack[-1]]:
                result.append(OPERATORS[stack.pop()])
            stack.append(i)
    for _ in range(len(stack)):
        result.append(OPERATORS[stack.pop()])
    return result


def result_of_expression(postfix_exp, variables):
    stack = []
    for i in range(len(postfix_exp)):
        if postfix_exp[i] in variables.keys():
            stack.append(variables[postfix_exp[i]])
        else:
            if postfix_exp[i] == 'not':
                stack.append(not stack.pop())
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append(eval(f'{var1} {postfix_exp[i]} {var2}'))
    return int(stack.pop())


statement = input()
var_all = sorted(set([i for i in statement if i.isupper()]))
print(' '.join(var_all), 'F')
table = product([0, 1], repeat=len(var_all))
statement = statement.replace('(', '( ').replace(')', ' )')
exp = postfix_expression(statement, var_all)

for row in table:
    res = {}
    for k, v in zip(var_all, row):
        res[k] = v
    print(' '.join(str(x) for x in row), result_of_expression(exp, res))