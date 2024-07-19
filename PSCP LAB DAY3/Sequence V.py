"""Sequence V"""
def main() :
    """Sequence V"""
    num = int(input())
    counter = 0
    for i in range(num ,0, -1) :
        counter += 1
        if counter >= 7 :
            counter = 0
            print(i)
        else :
            print(i , end=" ")
main()
