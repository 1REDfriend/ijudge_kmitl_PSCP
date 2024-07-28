"""Restaurant"""
def main():
    """Restaurant"""
    my_price = float(input())
    promo_price = float(input())
    discout = float(input())
    more_price = float(input())

    if discout <= 0 or more_price <= 0 or (my_price + more_price) < promo_price:
        print("Yes")
    else :
        if my_price + more_price >= promo_price :
            dis_price = (my_price + more_price) * (discout/100)
            dis_price = (my_price+more_price) - dis_price
            if dis_price > my_price :
                print(f"No {dis_price - my_price:.3f}")
            else :
                print(f"Yes {my_price - dis_price:.3f}")
        else :
            dis_price = my_price * (discout/100)
            dis_price = my_price - dis_price
            print(f"Yes {my_price - dis_price:.3f}")
main()
