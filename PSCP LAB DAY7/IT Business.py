"""IT Business"""
def main():
    """IT Business MAIN"""
    bank = int(input())
    cash = int(input())
    money = " "

    while True:
        money = input().split(" ")
        if money == "end":
            break
        if money[0] == "D":
            if cash >= int(money[1]):
                cash -= int(money[1])
                bank += int(money[1])
        elif money[0] == "W":
            if bank >= int(money[1]):
                bank -= int(input())
                cash += int(input())
    print(f"{bank:.2f}")
    print(f"{cash:.2f}")
main()
