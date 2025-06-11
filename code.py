# 이경석 학생 코드

op = ''

while op!='exit':
    op = input('식(4 + 6)를 입력하세요.종료하려면 exit:')
    if op.split()[1] == '+':
        print(int(op.split()[0]) + int(op.split()[2]))
    elif op.split()[1] == '-':
        print(int(op.split()[0]) - int(op.split()[2]))
    elif op.split()[1] == '*':
        print(int(op.split()[0]) * int(op.split()[2]))
    elif op.split()[1] == '/':
        if op.split()[2] == '0':
           print('0으로 나눌수 없습니다')
        else:
            print(float(op.split()[0]) / float(op.split()[2]))
    else:
        print('잘못 입력하셨습니다')