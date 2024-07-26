"""Restaurant"""
def main():
    """Restaurant"""
    my_price = float(input())
    promo_price = float(input())
    discout = float(input())
    more_price = float(input())

    if my_price + more_price < promo_price :
        print("Yes")
    else :
        dis_price = (my_price + promo_price) * (discout/100)
        if dis_price > my_price :
            print(f"No {dis_price - my_price:.2f}")
        else :
            print(f"Yes {my_price - dis_price:.2f}")
main()
