"""Circular I"""
def main() :
    """Circular I"""
    x = float(input())
    y = float(input())
    r = float(input())
    xd = float(input())
    yd = float(input())

    process = (((xd-x)**2) + ((yd-y)**2))**0.5
    if process <= r*2 :
        print("Yes")
    else :
        print("No")
main()
