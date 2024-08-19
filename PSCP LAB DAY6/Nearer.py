"""Nearer"""
def main() :
    """main"""
    alice = int(input())
    bob = int(input())
    ice = int(input())

    aliceCount = abs(alice - ice)
    bobCount = abs(bob - ice)

    if aliceCount < bobCount:
        print(f"Alice {aliceCount}")
    elif bobCount < aliceCount:
        print(f"Bob {bobCount}")
    else :
        print("Sundaes 0")
main()
