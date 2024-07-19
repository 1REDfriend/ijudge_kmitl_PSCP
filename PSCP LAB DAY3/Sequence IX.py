"""Sequence IX"""
def main() :
    """Sequence IX"""
    num = int(input())
    for i in range(1,num + 1) :
        space = "   "* (num - i)
        print(space , end="")
        for x in range(1 , i) :
            print(f"{x:02d}", end=" ")
        for x in range(i , 0 , -1) :
            print(f"{x:02d}" , end=" ")
        print()
main()
