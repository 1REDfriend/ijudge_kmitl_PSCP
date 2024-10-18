"""Seeker"""
def main() :
    """Seeker main"""
    txt = input() + "end"
    num = ""
    num_list = []

    for i in txt :
        if i.isnumeric() :
            num += i

        else :
            num_list.append((num))
            num = ""

    num_list = [x for x in num_list if x]
    num_list = list(map(int,num_list))

    print(sum(num_list))

main()
