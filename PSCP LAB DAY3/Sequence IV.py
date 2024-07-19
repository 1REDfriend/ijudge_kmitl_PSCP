"""Sequence IV"""
def main() :
    """Sequence IV"""
    num = int(input())
    mr_beast = 1
    for _ in range(num) :
        for i in range(mr_beast , num + mr_beast) :
            print(i, end=" ")
        print()
        mr_beast += num
main()
