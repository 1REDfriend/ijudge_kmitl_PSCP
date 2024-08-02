"""Hamburger"""
def main():
    """Hamburger"""
    num1 = int(input())
    num2 = int(input())
    x = "|"*num1
    y = "*"*((num1+num2)*2)
    z = "|"*num2
    print(f"{x}{y}{z}")
main()
