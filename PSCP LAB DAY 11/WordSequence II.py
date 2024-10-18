"""WordSequence II"""
def main() :
    """WordSequence II main"""
    txt1 = list(input())
    txt2 = list(input())
    min_txt = min(len(txt1),len(txt2))
    count = 0

    print("".join(txt1))
    while count < min_txt :
        if txt1 != txt2 :
            txt1[count] = txt2[count]
        count += 1
        print("".join(txt1))

    if len(txt1) > len(txt2) :
        while txt1 != txt2 :
            txt1.pop(count)
            print("".join(txt1))

    elif len(txt1) < len(txt2) :
        while txt1 != txt2 :
            txt1.append(txt2[count])
            count += 1
            print("".join(txt1))

main()
