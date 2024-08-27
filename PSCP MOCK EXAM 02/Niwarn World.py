"""Niwarn World"""
import math
def x(n) :
    """x"""
    return 2+(math.log2(n**2)/((2*n)*math.log2(n)))
def y(n,s) :
    """y"""
    return (math.sin(math.radians(30))+ ((2*s)**0.5))/(x(n)+3)
def z(k) :
    """z"""
    return y(k,k)**2 + ((8456*(x(k)**4))/(24*k))
def main() :
    """Niwarn World main"""
    n = float(input())
    s = float(input())
    k = float(input())

    print(f'X: {x(n):.1f}, Y: {y(n,s):.1f}, Z: {z(k):.1f}')
main()
