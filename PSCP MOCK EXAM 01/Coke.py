"""Coke"""
def main() :
    """Coke main"""
    coke_prices = int(input())
    need_lib = int(input())
    new_c_price = int(input())
    need_coke = int(input())

    paid = 0

    while need_coke :
        if need_coke >= need_lib :
            need_coke -= need_lib
            paid += coke_prices * need_lib
            if need_coke > 0 :
                need_coke -= 1
                paid += new_c_price
        else :
            paid += need_coke * coke_prices
            need_coke = 0
    print(paid)
main()
