"""Debaratna Road"""
def main() :
    """Debaratna Road mian"""
    km = float(input())
    if 58.855 >= km > 52.900 :
        print("Chon Buri")
    elif 58.855 >= km > 35.477 :
        print("Chachoengsao")
    elif 58.855 >= km > 5.032 :
        print("Samut Prakarn")
    elif 58.855 >= km >= 0 :
        print("Bangkok")
    else :
        print("InValid")
main()
