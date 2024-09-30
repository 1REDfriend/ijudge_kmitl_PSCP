"""Cat Parade"""
def cat(name , parade_list : list , counter) :
    """cat"""
    for i in name:
        if i != "END":
            if i != "IT'S A DOG":
                found = False
                for j,_ in enumerate(parade_list):
                    if parade_list[j][0] == i:
                        parade_list[j][2] += 1
                        found = True
                        break
                if not found:
                    parade_list.append([i,counter, 1])
                counter += 1
            else:
                if parade_list:
                    parade_list.pop()
                counter -= 1
        else:
            break
    return parade_list , counter
def main() :
    """Cat Parade main"""
    parade_list = []
    parade_sort = []
    counter = 1

    while True:
        name = input().split(", ")
        if "END" not in name:
            parade_list , counter= cat(name, parade_list,counter)
        else:
            break
    parade_sort = sorted(parade_list,key=lambda x : x[0])
    for i in parade_sort :
        print(f"{i[0]} {i[1]} {i[2]}")
main()
