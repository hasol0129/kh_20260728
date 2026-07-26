import random

def slot():
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