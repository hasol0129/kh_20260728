import random

def slot():

    while True:

        print("=== 슬롯머신 ===")

        game = ["🍒", "🍋", "⭐", "7", "🍉"]

        a = random.choice(game)
        b = random.choice(game)
        c = random.choice(game)

        print(f"[ {a} ] [ {b} ] [ {c} ]")

        if a == b == c:
            print("🎉 JACKPOT!")

        elif a == b or b == c or a == c:
            print("😊 2개 일치!")

        else:
            print("💀 꽝!")

        retry = input("다시 하시겠습니까? (y/n) : ").lower()

        if retry == "y":
            continue
        else:
            print("상위 메뉴로 돌아갑니다.")
            break