"""ijdriird"""

def main() :
    """isofjeejosof"""
    food_price = float(input())
    service_charge = 0
    if food_price * 0.1 < 50 :
        service_charge = 50
    elif food_price * 0.1 > 1000:
        service_charge = 1000
    else :
        service_charge = food_price * 0.1
    all_price = (food_price+service_charge) * 1.07

    print(f"{all_price:.2f}")

main()
