"""Lotto"""
def moreorless(num) :
    """find num if > 999999 or < 000000"""
    if num > 999999 :
        num = "000000"
    elif num < 0 :
        num = "999999"
    return str(num).zfill(6)

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
    win1_minus = moreorless(int(win1)-1)
    win1_plus = moreorless(int(win1)+1)

    if lotto == win1 :
        result += 6_000_000
    if lotto == win1_minus and lotto == win1_plus :
        result += 200_000
    elif lotto in (win1_minus , win1_plus) :
        result += 100_000
    if lotto[-2:] == winLast2 :
        result += 2_000
    if lotto[:3] == winFirst3_1 and lotto[:3] == winFirst3_2 :
        result += 8_000
    elif lotto[:3] == winFirst3_1 or lotto[:3] == winFirst3_2 :
        result += 4_000
    if lotto[-3:] == winLast3_1 and lotto[-3:] == winLast3_2 :
        result += 8_000
    elif lotto[-3:] == winLast3_1 or lotto[-3:] == winLast3_2 :
        result += 4_000
    print(result)
main()
