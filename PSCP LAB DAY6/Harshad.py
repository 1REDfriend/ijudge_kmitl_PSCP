"""Harshad"""
def main() :
    """Harshad main"""
    for _ in range(10):
        textNum = str(abs(int(input())))
        temp1 = 0
        if textNum == "0" :
            print("No")
            continue
        for i in textNum :
            temp1 += int(i)
        if not int(textNum) % temp1 :
            print("Yes")
        else :
            print("No")
main()
