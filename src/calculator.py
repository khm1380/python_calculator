from src.tokenizer import tokenize as tk


def calculate(user_input: str) -> int | float | str:
    """
    @param user_input: 수식 문자열
    @return: 계산 결과 또는 오류 메시지
    """

    tokens = tk(user_input)
    if not tokens: return "잘못된 수식입니다."

    # 연산자 우선 순위 (높은 숫자 부터)
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    ops = []
    output = []

    # 중위 -> 후위
    for token in tokens:
        if token.replace('.', '', 1).lstrip('-').isdigit():  # - 부호 때고, 문자열이 숫자로 구성 되었는지
            output.append(token)

        # 현재 토큰이 연산자 인지 확인하기
        elif token in precedence:
            # 스택이 비어있지 않고, top이 여는 괄호가 아니고
            # 스택 상단 연산자 우선순위가 현재 우선순위 이상인 동안 반복해서 꺼내기
            while (
                    ops and
                    ops[-1] != '(' and
                    precedence.get(ops[-1], 0) >= precedence[token]
            ):
                output.append(ops.pop())
            ops.append(token)

        elif token == '(':
            ops.append(token)

        elif token == ')':
            # 열린 괄호 나올떄 까지 pop 해서 출력
            while ops and ops[-1] != '(':
                output.append(ops.pop())

            # 괄호 짝 체크
            if ops and ops[-1] == '(':
                ops.pop()
                # output.append('*')
            else:
                return "괄호 오류"
        else:
            return "잘못된 토큰 포함"

    while ops:
        if ops[-1] in '()':  # 남은 괄호가 있을 경우
            return "괄호 오류"
        output.append(ops.pop())

    # 후위 계산
    stack = []
    for token in output:
        if token.replace('.', '', 1).lstrip('-').isdigit():
            stack.append(float(token) if '.' in token else int(token))
        else:
            if len(stack) < 2:
                return "연산 오류"

            b = stack.pop()  # 후 출력 스택, 우측 피연산자
            a = stack.pop()  # b의 반대

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

    if len(stack) != 1: return "오류"  # 스택에는 연산 값만 한개 남아있어야 함

    res = stack[0]

    if res == int(res):
        return int(res)

    return res
