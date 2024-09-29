"""Netflix"""
def check(count_mobile, count_basic, count_standard, count_premium, alls) :
    """check"""
    if count_premium :
        print(f"Premium x {count_premium}")
    if count_standard :
        print(f"Standard x {count_standard}")
    if count_basic :
        print(f"Basic x {count_basic}")
    if count_mobile :
        print(f"Mobile x {count_mobile}")
    print(f"Total = {alls} THB")

def main() :
    """Netflix main"""

    num_screens = int(input())
    num_device = int(input())
    unlimited =  input()
    wat_mobile = input()
    wat_tv = input()
    hd = input()
    uhd = input()

    unlimited += ""
    wat_mobile += ""

    count_mobile = 0
    count_basic = 0
    count_standard = 0
    count_premium = 0

    alls = 0

    while num_device > 0 and num_screens > 0 :
        if (wat_tv == "Yes" or hd == "Yes" or uhd == "Yes") and (num_screens >= 3 or num_device >= 3) :
            alls += 419
            count_premium += 1
            num_device -= 4
            num_screens -= 4
        elif (wat_tv == "Yes" or hd == "Yes") and (num_screens >= 2 or num_device >= 2) :
            alls += 349
            count_standard += 1
            num_device -= 2
            num_screens -= 2
        elif wat_tv == "Yes" and hd == "No" and uhd == "No" :
            alls += 279
            count_basic += 1
            num_device -= 1
            num_screens -= 1
        else :
            if uhd == "Yes" :
                alls += 419
                count_premium += 1
                num_device -= 4
                num_screens -= 4
            elif hd == "Yes" :
                alls += 349
                count_standard += 1
                num_device -= 2
                num_screens -= 2
            elif wat_tv == "Yes" :
                alls += 279
                count_basic += 1
                num_device -= 1
                num_screens -= 1
            else :
                alls += 99
                count_mobile += 1
                num_device -= 1
                num_screens -= 1

    check(count_mobile, count_basic, count_standard, count_premium, alls)

main()
