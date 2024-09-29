"""Coke"""
def main() :
    """Coke main"""
    coke_price = int(input())
    need_lib = int(input())
    new_price = int(input())
    need = int(input())

    lib = 0

    result = 0

    while need > 0 :
        need -= 1
        lib += 1
        result += coke_price
        while lib >= need_lib and need > 0 and need_lib and coke_price :
            lib -= need_lib
            need -= 1
            result += new_price
            lib += 1
    print(result)
main()
