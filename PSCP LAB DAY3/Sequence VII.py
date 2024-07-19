"""Sequence VII"""
def main() :
    """Sequence VII"""
    num = int(input())
    for i in range(1 , num + 1) :
        for x in range(1, i+1) :
            print(x, end=" ")
        print()
    for i in range(num-1 , 0 , -1) :
        for x in range(1,i+1) :
            print(x,end=" ")
        print()
main()
