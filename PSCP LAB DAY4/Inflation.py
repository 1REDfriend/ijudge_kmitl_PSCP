"""Inflation"""
def main():
    """main"""
    num = int(float(input())*100)
    year = int(input())

    for _ in range(year) :
        num = int(num * (3.81/100))
    num /= 100
    print(f"{num:.2f}")
main()
