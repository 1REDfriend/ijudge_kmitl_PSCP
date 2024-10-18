"""LetterFrequency"""
def main() :
    """LetterFrequency main"""
    txt = input().strip().lower().replace(" ", "")

    dt = {}

    for i in txt :
        if i in dt :
            dt[i] += 1
        else :
            dt[i] = 1

    dt = dict(sorted(dt.items(),key=lambda item: item[1] , reverse=True))
    print(next(iter(dt)))
main()
