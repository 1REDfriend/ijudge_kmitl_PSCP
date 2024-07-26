"""Right Arrow"""
def main() :
    """main"""
    lenth = int(input())
    num =  int(input())
    for i in range(num//2, 0 , -1) :
        print(f"{' '*((num//2)-i)}{'*'*lenth}")
    for i in range(num//2 + 1) :
        print(f"{' '*((num//2)-i)}{'*'*lenth}")
main()
