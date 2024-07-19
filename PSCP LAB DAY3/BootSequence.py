"""BootSequence"""
def main() :
    """BootSequence"""
    num = int(input())
    num_list = []
    for i in range(1,num+1) :
        num_list.append(str(i))
        num_list.append("_")
    num_list.pop()
    print("".join(num_list))
main()
