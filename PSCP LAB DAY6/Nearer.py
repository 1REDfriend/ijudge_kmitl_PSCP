"""Nearer"""
def main() :
    """main"""
    alice = int(input())
    bob = int(input())
    ice = int(input())

    if alice < 0 :
        alice = abs(alice) + 1
    if bob < 0 :
        bob = abs(bob) + 1
    if ice < 0 :
        ice = abs(ice) + 1

    if abs(alice - ice) < abs(bob - ice) :
        print("Alice" , abs(alice - ice))
    elif abs(bob - ice) < abs(alice - ice) :
        print("Bob" , abs(bob - ice))
    else :
        print("Sundaes")
main()
