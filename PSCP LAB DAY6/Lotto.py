"""Lotto"""
def main() :
    """Lotto main"""
    win1 = input().zfill(6)
    winLast2 = input().zfill(2)
    winFirst3_1 = input().zfill(3)
    winFirst3_2 = input().zfill(3)
    winLast3_1 = input().zfill(3)
    winLast3_2 = input().zfill(3)
    lotto = input().zfill(6)

    result = 0
    win1_minus = str(int(win1)-1).zfill(6)
    win1_plus = str(int(win1)+1).zfill(6)
    if win1_minus == "-000001" :
        win1_minus = "999999"

    if lotto == win1 :
        result += 6_000_000
    if lotto == win1_minus or lotto == win1_plus :
        result += 100_000
    if lotto[-2:] == winLast2 :
        result += 2_000
    if lotto[:3] == winFirst3_1 or lotto[:3] == winFirst3_2 :
        result += 4_000
    if lotto[-3:] == winLast3_1 or lotto[-3:] == winLast3_2 :
        result += 4_000
    print(result)
main()
