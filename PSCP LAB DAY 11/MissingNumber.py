"""MissingNumber"""
def main() :
    """MissingNumber main"""

    set_a = set()
    set_b = set()

    for i in range(1,int(input())+1) :
        set_a.add(i)

    while True :
        num = int(input())
        if not num :
            break
        set_b.add(num)

    del_set = sorted(set_a - set_b)

    for i in del_set :
        print(i)

main()
