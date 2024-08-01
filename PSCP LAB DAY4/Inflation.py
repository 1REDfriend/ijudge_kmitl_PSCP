"""Inflation"""
def main():
    """main"""
    num = float(input())
    year = int(input())
    inflation_rate = 0.0381

    num = str(num)
    dot = num.find(".")
    if dot != -1 :
        num = num[:dot+3]
    num = float(num)

    for _ in range(year) :
        num = (num * (1 + inflation_rate)) * 100
        num = str(num)
        dot = num.find(".")
        if dot != -1 :
            num = num[:dot]
        print(num)
        num = int(num)
    print(f"{num/100}")
main()
