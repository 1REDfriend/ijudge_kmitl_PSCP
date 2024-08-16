"""Stamps"""
def main() :
    """Stamps main"""
    eatCount = int(input())
    needSaid = int(input())
    stamp = int(input())
    needStamp = int(input())
    discount = int(input())

    stampStack = 0
    result = 0
    discountNow = 0

    for _ in range(eatCount) :
        foodPrice = int(input())

        stampStack += (foodPrice//needSaid) * stamp
        while stampStack >= needStamp :
            stampStack -= needStamp
            discountNow += discount
        temp = foodPrice-discountNow
        if temp >= 0 :
            result += temp
    print(result)
    print(stampStack)
main()
