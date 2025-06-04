from src.tokenizer import tokenize as tk

def calculate(expr):
    tokens = tk(expr)
    if not tokens:
        return "잘못된 수식입니다."

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    ops = []

    for token in tokens:
        if token.replace('.', '', 1).lstrip('-').isdigit():
            output.append(token)
        elif token in '+-*/':
            while ops and ops[-1] != '(' and precedence.get(ops[-1], 0) >= precedence[token]:
                output.append(ops.pop())
            ops.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(': 
                output.append(ops.pop())
            if ops and ops[-1] == '(':
                ops.pop()
            else:
                return "괄호 오류"
        else:
            return "잘못된 토큰 포함"

    while ops:
        if ops[-1] in '()':
            return "괄호 오류"
        output.append(ops.pop())

    stack = []
    for token in output:
        if token.replace('.', '', 1).lstrip('-').isdigit():
            stack.append(float(token) if '.' in token else int(token))
        else:
            if len(stack) < 2:
                return "연산 오류"
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    return "0으로 나눌 수 없습니다."
                stack.append(a / b)

    result = stack[0]
    return int(result) if result == int(result) else result