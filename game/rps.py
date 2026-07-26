import random

def rps():
    print("=== 가위바위보 ===")

    game = ["가위", "바위", "보"]

    com = random.choice(game)
    user = input("가위/바위/보 입력 : ")

    print(f"컴퓨터 : {com}")
    print(f"나 : {user}")

    if com == user:
        print("🤝 무승부!")

    elif (user == "가위" and com == "보") or \
         (user == "바위" and com == "가위") or \
         (user == "보" and com == "바위"):
        print("🎉 승리!")

    else:
        print("패배!..")