import random

def updown():

    while True:

        print("=== 업다운 ===")

        answer = random.randint(1, 100)

        while True:
            user = int(input("1~100 입력 : "))

            if user > answer:
                print("⬇️ DOWN")

            elif user < answer:
                print("⬆️ UP")

            else:
                print("🎉 정답!")
                break

        retry = input("다시 하시겠습니까? (y/n) : ").lower()

        if retry == "y":
            continue
        else:
            print("상위 메뉴로 돌아갑니다.")
            break