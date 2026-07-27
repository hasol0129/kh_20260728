from game.rps import rps
from game.updown import updown
from game.lotto import lotto
from game.slot import slot

while True:

    print("\n===== 🎮 미니 게임 =====")
    print("1. 가위바위보")
    print("2. 업다운")
    print("3. 로또 게임")
    print("4. 슬롯머신")
    print("5. 종료")

    menu = input("메뉴 선택 : ")

    if menu == "1":
        rps()

    elif menu == "2":
        updown()

    elif menu == "3":
        lotto()

    elif menu == "4":
        slot()

    elif menu == "5":
        print("👋게임을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다.")