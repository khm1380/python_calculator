def tokenize(user_input: str) -> list[str] | None:
    tokens: list[str] = []
    num = ''
    prev = ''

    i = 0

    while i < len(user_input):
        char = user_input[i]

        if char.isdigit() or char == '.':
            num += char
        elif char in "+-*/":
            if num:
                tokens.append(num)
                num = ''
            is_unary = char == '-' and (prev in "+-*/(" or prev == '' or i == 0)

            if is_unary:
                if i + 1 < len(user_input) and user_input[i + 1] == '(':  # '-(' 패턴
                    tokens.append('-1')
                    tokens.append('*')
                else:
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
            tokens.append('(')
        elif char == ')':
            if num:
                tokens.append(num)
                num = ''
            tokens.append(')')
            if i + 1 < len(user_input) and user_input[i + 1].isdigit():
                tokens.append('*')
        else:
            return None

        if char not in "0123456789.":
            prev = char
        i += 1

    if num:
        tokens.append(num)
    return tokens
