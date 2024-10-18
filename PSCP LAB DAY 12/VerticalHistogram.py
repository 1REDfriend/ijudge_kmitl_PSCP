"""VerticalHistogram"""
def main() :
    """VerticalHistogram main"""
    txt_bage = sorted(input().strip().replace(" ", ""))

    dt = {}

    for i in txt_bage :
        if i.isalpha() :
            if i in dt :
                dt[i] += 1
            else :
                dt[i] = 1

    max_num = max(dt.values())
    len_maxnum = len(str(max_num))
    for i in range(max_num,0 , -1) :
        print(i, end="  ")
        for _,v in dt.items() :
            print("*" if v >= i else " ", end=" ")
        print()
    print("   " , end="")

    for k,_ in dt.items() :
        print(k,end=" ")
main()
