import random

def updown():
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