"""Milk"""
def main() :
    """MilkMilkMilkMilkMilk"""
    milk_price = int(input())
    lib_promo = int(input())
    free_milk = int(input())
    money = int(input())

    lib_promo_temp = lib_promo
    has_promo = 0
    my_milk = 0

    # จะมีการนำขวดที่ได้จากการแลกมาแลกอีก
    if lib_promo :
        while lib_promo * milk_price <= money :
            my_milk += lib_promo + free_milk
            money -= lib_promo * milk_price
            lib_promo = lib_promo_temp - free_milk
            has_promo = 1
        lib_promo_temp = lib_promo
        while money >= milk_price :
            money -= milk_price
            my_milk += 1
            lib_promo -= 1
            if lib_promo_temp <= 0 :
                my_milk += free_milk
                lib_promo_temp = lib_promo
                if not has_promo :
                    lib_promo_temp -= free_milk
                    has_promo = 1
    else :
        while money >= milk_price :
            money -= milk_price
            my_milk += 1
    print(my_milk)
main()
