def tokenize(expr):
    tokens = []
    num = ''

    for char in expr:
        if char in "0123456789.":
            num += char
        elif char in "+-*/":
            if num:
                tokens.append(num)
                num = ''
            tokens.append(char)
        else:
            return None
    if num:
        tokens.append(num)

    return tokens