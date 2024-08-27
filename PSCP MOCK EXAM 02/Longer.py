"""Longer"""
import math
def main() :
    """Longer main"""
    r = float(input())
    a = float(input())
    b = float(input())

    rectangle = a*2+b*2
    circle = 2 * math.pi * r

    if rectangle > circle :
        print('Rectangle is longer')
        print(f'{rectangle-circle:.5f}')
    elif circle > rectangle :
        print('Circle is longer')
        print(f'{circle-rectangle:.5f}')
    else :
        print('Equal')
        print(f'{0:.5f}')
main()
