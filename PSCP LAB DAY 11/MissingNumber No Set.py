"""MissingNumber No Set"""
def main() :
    """MissingNumber No Set main"""
    num_list = []
    most = int(input())

    while True :
        num = int(input())
        if not num :
            break
        num_list.append(num)

    for i in range(1,most+1) :
        if i not in num_list :
            print(i)
main()
