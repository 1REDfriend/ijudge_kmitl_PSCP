"""Squid Game 3 - Tug-of-War"""
def main():
    """Squid Game 3 - Tug-of-War MAIN"""
    a_power = 0
    b_power = 0
    for _ in range(10):
        a_power += int(input())
    for _ in range(10):
        b_power += int(input())
    if a_power > b_power:
        print("B")
    elif b_power > a_power:
        print("A")
    else:
        print("AB")
main()
        