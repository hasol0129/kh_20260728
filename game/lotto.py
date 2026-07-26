import random

def lotto():

    while True:

        print("=== 로또 ===")

        num = random.sample(range(1, 46), 6)
        num.sort()

        print("🎰 이번 주 번호")
        print(num)

        retry = input("다시 하시겠습니까? (y/n) : ").lower()

        if retry == "y":
            continue
        else:
            print("상위 메뉴로 돌아갑니다.")
            break