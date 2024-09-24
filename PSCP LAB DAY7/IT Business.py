"""IT Business"""
def main():
    """IT Business MAIN"""
    bank = float(input())
    cash = float(input())
    money = " "
    count = 0

    while True:
        money = input()
        if money == "end":
            break
        if money[:money.find(" ")] == "D":
            if cash >= float(money[money.find(" "):]):
                cash -= float(money[money.find(" "):])
                bank += float(money[money.find(" "):])
                count = 0
            else :
                count += 1
        elif money[:money.find(" ")] == "W":
            if bank >= float(money[money.find(" "):]):
                bank -= float(money[money.find(" "):])
                cash += float(money[money.find(" "):])
                count = 0
            else :
                count += 1
        else :
            count += 1
        if count >= 3 :
            break
    print(f"{bank:.2f}")
    print(f"{cash:.2f}")
main()
