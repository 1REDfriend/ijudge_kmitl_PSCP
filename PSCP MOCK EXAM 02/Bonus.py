"""Bonus"""
def main() :
    """Bonus main"""
    money = int(input())
    year=  int(input())
    month = int(input())
    if month >= 10 :
        month -= 10
        year += 1
    bonus = money * year
    if bonus > money * 20 :
        bonus = money * 20
    if bonus > 1_000_000 :
        bonus = 1_000_000
    if bonus < 5000 :
        bonus = 5_000
    print(bonus)
main()
