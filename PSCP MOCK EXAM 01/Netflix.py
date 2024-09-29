"""Netflix"""
def check(c_mobile, c_basic, c_standard, c_premium, total) :
    """check"""
    if c_premium :
        print(f"Premium x {c_premium}")
    if c_standard :
        print(f"Standard x {c_standard}")
    if c_basic :
        print(f"Basic x {c_basic}")
    if c_mobile :
        print(f"Mobile x {c_mobile}")
    print(f"Total = {total} THB")

def num_max(num, w_tv, hd, uhd) :
    """num device or screen"""
    c_mobile = 0
    c_basic = 0
    c_standard = 0
    c_premium = 0
    total = 0
    if w_tv == "Yes" and num >= 3 :
        n = num // 4
        total += 419 * n
        c_premium += n
        num -= n * 4
        if w_tv == "Yes" and num >= 3 :
            c_premium += 1
            total += 419
            num -= 4
    if w_tv == "Yes" and uhd == "No" and num >= 2 :
        n = num // 2
        total += 349 * n
        c_standard += n
        num -= n * 2
    if w_tv == "Yes" and hd == "No" and uhd == "No" and num == 1 :
        total += 279 * num
        c_basic += num
        num = 0
    if uhd == "Yes" and num > 0 :
        total += 419
        c_premium += 1
    elif hd == "Yes" and num > 0 :
        total += 349
        c_standard += 1
    elif w_tv == "Yes" and num > 0 :
        total += 279
        c_basic += 1
    elif num > 0 :
        total += 99 * num
        c_mobile += num
    check(c_mobile, c_basic, c_standard, c_premium, total)

def main() :
    """Netflix main"""

    num_screens = int(input())
    num_device = int(input())
    u_movie = input()
    w_mobile= input()
    w_tv = input()
    hd = input()
    uhd = input()

    u_movie += ""
    w_mobile+= ""
    if num_device > num_screens :
        num_max(num_device, w_tv, hd, uhd)
    else :
        num_max(num_screens, w_tv, hd, uhd)
main()
