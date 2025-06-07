def tokenize(expr):
    tokens = []
    num = ''
    prev = ''

    i = 0
    while i < len(expr):
        char = expr[i]

        if char in "0123456789.":
            num += char

        elif char in "+-*/":
            if num:
                tokens.append(num)
                num = ''
            if char == '-' and (prev in "+-*/(" or prev == '' or i == 0):
                num += char
            else:
                tokens.append(char)

        elif char == '(':
            if num:
                tokens.append(num)
                tokens.append('*')
                num = ''
            elif tokens and tokens[-1] == ')':
                tokens.append('*')
            tokens.append(char)

        elif char == ')':
            if num:
                tokens.append(num)
                num = ''
            tokens.append(char)
            if i + 1 < len(expr) and expr[i + 1] in "0123456789":
                tokens.append('*')

        else:
            return None

        if char not in "0123456789.":
            prev = char

        i += 1

    if num:
        tokens.append(num)

    return tokens
