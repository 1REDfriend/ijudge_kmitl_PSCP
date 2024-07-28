"""Inflation"""
def main():
    """main"""
    num = float(input())
    year = int(input())
    inflation_rate = 0.0381

    for _ in range(year) :
        num = num * (1 + inflation_rate)
        num = int(num * 100) / 100
        print(num)
    print(f"{num}")
main()
