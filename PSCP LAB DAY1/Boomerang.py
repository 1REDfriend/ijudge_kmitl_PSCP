"""Boomerang"""
def main():
    """Boomerang"""
    x = int(input())
    y = int(input())
    z = int(input())
    fx = x + 1
    fy = 7*(y**3) + 2*(y**2) - 31*(y) + 1
    fz = -z
    fxy = (x + y)*(x - y)
    fxyz = (y - ((y**2) - 4*x*z)**0.5)/(2*x)
    print(fx)
    print(fy)
    print(fz)
    print(fxy)
    print(fxyz)
main()
