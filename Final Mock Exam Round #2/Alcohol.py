"""Alcohol"""
def male_c (al, kg) :
    """male caculator"""
    return al/(kg * 6.8)

def female_c (al, kg) :
    """female caculator"""
    return al/(kg * 5.5)

def cal(al , cc) :
    """cal al"""
    return (al*cc)/100

def main() :
    """Alcohol main"""
    gender = input()
    weight = float(input())
    licen = input()
    cc = float(input())
    al = float(input())
    count = int(input())
    h_wait = float(input())

    if gender == "Male" :
        mmp = (cal(al,cc)*count) 
        mm = male_c(mmp, weight) - 0.015*h_wait
        if mm <= 0.05 and licen == "Yes":
            print("Safe")
        else :
            print("Not Safe")

    elif gender == "Female" :
        mmp = (cal(al,cc)*count)
        mm = female_c(mmp, weight) - 0.015*h_wait
        if mm <= 0.05 and licen == "Yes" :
            print("Safe")
        else :
            print("Not Safe")
    else :
        print("Not Safe")
main()
