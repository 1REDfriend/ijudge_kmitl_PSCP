"""diamond"""
def main() :
    """diamond main"""
    num = int(input())
    print(f'{" "*(num//2)}*')
    for i in range(1,(num//2)) :
        print(f'{" "*((num//2)-i)}*{" "*((i*2)-1)}*')
    print("*"*num)
    for i in range((num//2)-1,0,-1) :
        print(f'{" "*((num//2)-i)}*{" "*((i*2)-1)}*')
    print(f'{" "*(num//2)}*')
main()
