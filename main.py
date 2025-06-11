from src.calculator import calculate as cal

def main():
    print("사용방법 : 1+2, 4*5-3, (3+4)*2, -5+2")
    print("종료하려면 'exit' 입력")

    while True:
        user_input = input(">> ").replace(" ", "") # 공백 제거

        if user_input.lower() == 'exit':
            print("계산기를 종료합니다.")
            break

        res = cal(user_input)
        print(f"결과: {res}")

if __name__ == "__main__":
    main()