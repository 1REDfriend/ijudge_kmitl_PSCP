"""Century"""
def main() :
    """Century main """
    num = int(input())
    for _ in range(num) :
        date = input().strip().split(" ")
        if date[0].upper() == "B.E." :
            engYear = int(date[1]) - 543
            engYear += 100
            century = engYear // 100
            two_century = str(engYear)[:2]
            if not engYear % 100 and str(century) in two_century :
                century -= 1
            if century <= 0 or century == float('inf'):
                print("ERROR")
                continue
            print(century)

        elif date[0].upper() == "A.D." :
            engYear = int(date[1]) + 100
            century = engYear // 100
            two_century = str(engYear)[:2]
            if not engYear % 100 and str(century) in two_century  :
                century -= 1
            if century <= 0 or century == float('inf'):
                print("ERROR")
                continue
            print(century)

        else :
            print("ERROR")
main()
