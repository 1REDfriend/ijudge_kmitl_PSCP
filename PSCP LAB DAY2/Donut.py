"""Donut"""
def main() :
    """Donut"""
    price = int(input())
    donut_promo = int(input())
    free_donut = int(input())
    need = int(input())

    best_price = 0
    my_donut = 0

    #หาโดนัทที่คิดจาก promotion แล้ว
    promo_donut = need // (donut_promo + free_donut)
    best_price = (promo_donut*(donut_promo))*price
    need -= promo_donut*(donut_promo+free_donut)
    my_donut = promo_donut*(donut_promo+free_donut)

    #หาอีกรอบ เพราะอาจจะได้ promotion ก็ได้ใครจะไปรู้ แต่ครั้งเดียวพอเดี่ยวขาดทุน
    while promo_donut > 0 :
        if need >= donut_promo :
            promo_donut = 1
            best_price += (promo_donut*(donut_promo))*price
            need -= promo_donut*(donut_promo)
            my_donut += promo_donut*(donut_promo+free_donut)
        else :
            promo_donut = 0

    #หลังจากนั้นซื้อโดนัทที่มีรู เป็นเงินโดยที่เราใช้ promotion ไปหมดแล้ว "_"
    if need > 0 :
        my_donut += need
        best_price += need * price
        need = 0
    print(best_price , my_donut)
main()
