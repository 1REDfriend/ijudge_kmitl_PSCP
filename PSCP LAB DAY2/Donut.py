"""Donut"""
def main() :
    """Donut"""
    price = int(input())
    donut_promo = int(input())
    free_donut = int(input())
    need = int(input())

    best_price = 0
    my_donut = 0
    donut_promo_temp = donut_promo

    #หาโดนัทที่คิดจาก promotion แล้ว
    promo_donut = need // (donut_promo + free_donut)
    best_price = (promo_donut*(donut_promo))*price
    need -= promo_donut*(donut_promo+free_donut)
    my_donut = promo_donut*(donut_promo+free_donut)

    #หาอีกรอบ เพราะอาจจะได้ promotion ก็ได้ใครจะไปรู้
    while need > 0 :
        my_donut += 1
        best_price += price
        donut_promo_temp -= 1
        need -= 1
        #หลังจากนั้นซื้อโดนัทที่มีรู เป็นเงินโดยที่เราใช้ promotion ไปหมดแล้วจริงหรือหลอก "_"
        if donut_promo_temp <= 0 :
            my_donut += free_donut
            donut_promo_temp = donut_promo
            need -= free_donut
    print(best_price , my_donut)
main()
