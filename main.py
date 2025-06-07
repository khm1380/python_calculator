from src.calculator import calculate as cal

def main():
    print("사용방법 : 1+2, 4*5-3, (3+4)*2, -5+2")
    print("종료하려면 'exit' 입력")

    while True:
        expr = input(">> ").replace(" ", "")
        if expr.lower() == 'exit':
            print("계산기를 종료합니다.")
            break
        result = cal(expr)
        print(f"결과: {result}")

if __name__ == "__main__":
    main()