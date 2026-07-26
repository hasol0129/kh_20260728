import random

def lotto():
    print("=== 로또 ===")

    num = random.sample(range(1, 46), 6)
    num.sort()

    print("🎰 이번 주 번호")
    print(num)