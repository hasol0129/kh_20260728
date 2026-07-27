import random

def lotto():

    while True:

        print("===== 로또 게임 =====")
        print("1. 로또 구매 ")
        print("2. 종료")

        menu = input("선택 : ")

        if menu == "1":

            print("\n로또를 구매했습니다!")

            input("엔터를 누르면 추첨합니다...")

            lotto = random.sample(range(1, 46), 6)
            lotto.sort()

            print("당첨 번호 :", lotto)

            prize = random.randint(1, 100)

            if prize <= 1:
                print("1등 당첨!!!")
            elif prize <= 5:
                print("2등 당첨!!")
            elif prize <= 15:
                print("3등 당첨!")
            else:
                print("아쉽지만 꽝입니다.")

        elif menu == "2":
            print("게임 종료")
            break

        else:
            print("잘못 입력했습니다.")