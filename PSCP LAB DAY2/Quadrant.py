"""Quadrant"""
def main() :
    """Quadrant"""
    x = int(input())
    y = int(input())
    if not x and not y :
        print("O")
    elif not x :
        print("Y")
    elif not y :
        print("X")
    elif x == abs(x) and y == abs(y) :
        print("Q1")
    elif not x == abs(x) and y == abs(y) :
        print("Q2")
    elif not x == abs(x) and not y == abs(y) :
        print("Q3")
    elif x == abs(x) and not y == abs(y) :
        print("Q4")
main()
