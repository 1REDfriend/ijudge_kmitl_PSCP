"""Cat Parade"""
def cat(name , parade_list : list) :
    """cat"""
    for i in name:
        if i != "END" :
            if i != "IT'S A DOG" :
                if parade_list[i] == -1 :
                    parade_list.append([i,1])
                else :
                    parade_list[parade_list[i]][1] += 1
            else :
                parade_list.pop()
        else :
            break
    return parade_list
def main() :
    """Cat Parade main"""
    parade_list = []
    parade_sort = []

    while True :
        name = input().split(", ")
        if name[0] != "END" :
            parade_list = cat(name , parade_list)
        else :
            break
    print(parade_list)
main()
    
