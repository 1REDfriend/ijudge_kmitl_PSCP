"""Left Arrow"""
def main() :
    """Main"""
    lenth = int(input())
    num =  int(input())
    for i in range(num//2) :
        print(f"{' '*((num//2)-i)}{'*'*lenth}")
    for i in range(num//2 , -1 , -1) :
        print(f"{' '*((num//2)-i)}{'*'*lenth}")
main()
