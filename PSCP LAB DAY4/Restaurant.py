"""Restaurant"""
def main():
    """Restaurant"""
    my_price = float(input())
    promo_price = float(input())
    discount = float(input())
    more_price = float(input())

    if my_price >= promo_price:
        print("Yes")
    else:
        total_price_with_more = my_price + more_price
        if total_price_with_more >= promo_price:

            discounted_price = total_price_with_more * (1 - discount / 100) # ราคาที่ได้ส่วนลด

            if discounted_price < my_price:
                if my_price - discounted_price <= 0 :
                    print("Yes")
                else :
                    print(f"Yes {my_price - discounted_price:.3f}")
            else:
                if discounted_price - my_price <= 0 :
                    print("Yes")
                else :
                    print(f"No {discounted_price - my_price:.3f}")
        else:
            print("Yes")
main()
