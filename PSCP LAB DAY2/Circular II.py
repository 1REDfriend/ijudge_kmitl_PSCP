"""Circular II"""
def main() :
    """Circular II"""
    x = float(input())
    y = float(input())
    r = float(input())
    xf = float(input())
    yf = float(input())
    rf = float(input())

    process = (((xf-x)**2) + ((yf-y)**2))**0.5
    if process <= (r+rf)*2:
        print("Yes")
    else :
        print("No")
main()
