"""Stamps"""
def main() :
    """Stamps main"""
    eatCount = int(input())
    needPaid = int(input())
    stampAdd = int(input())
    needStamp = int(input())
    discount = int(input())

    stampStack = 0
    result = 0
    use_stamp = False

    for _ in range(eatCount) :
        iPaid = int(input())
        if stampStack >= needStamp and needStamp:
            pay = iPaid
            while stampStack >= needStamp :
                stampStack -= needStamp
                pay -= discount
                if pay <= 0 :
                    break
            if pay > 0 :
                result += pay
            use_stamp = True
        if iPaid >= needPaid and needPaid:
            stampStack += (iPaid // needPaid ) * stampAdd
        if not use_stamp :
            result += iPaid
        use_stamp = False
    print(result)
    print(stampStack)
main()
