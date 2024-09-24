"""Stamps"""
def main():
    """Stamps main"""

    num = int(input())
    price_need = int(input())
    stamp_add = int(input())
    stamp_need = int(input())
    discount = int(input())

    count=0
    all_pay = 0

    for _ in range(num):
        pay = int(input())
        if count >= stamp_need:
            while pay > 0 and count > 0 and count-stamp_need >= 0:
                pay = max(pay - discount,0)
                count -= stamp_need
        all_pay += pay
        count += (pay//price_need)*stamp_add
    print(all_pay,count,sep="\n")

main()
