"""Day I"""
def main() :
    """Day I"""
    year = int(input())
    if year // 4 == year / 4 :
        if year // 100 == year / 100 :
            if year // 400 == year / 400 :
                print("Yes")
            else :
                print("No")
        else :
            print("Yes")
    else :
        print("No")
main()
