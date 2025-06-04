from src.tokenizer import tokenize as tk

def calculate(expression):
    tokens = tk(expression)

    if not tokens:
        return "잘못된 수식 입니다."
    
    result = None
    operation = None

    for token in tokens:
        if token in "+-*/":
            operation = token
        else:
            try:
                num = float(token)
            except ValueError:
                return f"잘못된 숫자: {token}"
            
            if result is None:
                result = num
            elif operation:
                if operation == '+':
                    result += num
                elif operation == '-':
                    result -= num
                elif operation == '*':
                    result *= num
                elif operation == '/':
                    if num == 0:
                        return "0으로 나눌 수 없습니다."
                    result /= num
                operation = None
            else:
                return "잘못된 수식입니다."
    
    return int(result) if result == int(result) else result