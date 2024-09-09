"""Coffee Shop"""
def choice_one(a,b,e) :
    """one"""
    result = a
    result += (a-(a*b/100))*(e-1)
    return result

def choice_two(a,c,d,e) :
    """two"""
    result = e*a
    if e*a >= d :
        result = e*a-((e*a)*c/100)
    return result

def main() :
    """Coffee Shops main"""
    cf_price = float(input())
    cf_promo2kub = float(input())
    cf_discount = float(input())
    cf_dis_price = float(input())
    cf_count = int(input())

    first_choice = choice_one(cf_price,cf_promo2kub,cf_count)
    last_choice = choice_two(cf_price,cf_discount,cf_dis_price,cf_count)

    if first_choice >= last_choice :
        print(2)
        print(f'{last_choice:.2f}')
    else :
        print(1)
        print(f'{first_choice:.2f}')
main()
