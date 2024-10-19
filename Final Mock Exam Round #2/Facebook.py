"""Facebook"""
def main() :
    """Facebook main"""
    friend = {}
    i_find = []
    while True :
        txt = input()
        txt = txt.split(" <-> ") if "<->" in txt else txt
        if all("?" not in x for x in txt) and txt:
            if txt[0] in friend :
                friend[txt[0]].append(txt[1])
            else :
                friend[txt[0]] = [txt[1]]
            if txt[1] in friend :
                friend[txt[1]].append(txt[0])
            else :
                friend[txt[1]] = [txt[0]]
        elif " ? " in txt:
            i_find = txt.split(" ? ")
            break

    if i_find and i_find[0] in friend and i_find[1] in friend:
        cross_friend = list(set(friend[i_find[0]]) & set(friend[i_find[1]]))
        cross_friend.sort()

        if cross_friend:
            for i in cross_friend:
                print(i.strip())
        else:
            print("No mutual friend")
    else:
        print("No mutual friend")
main()
