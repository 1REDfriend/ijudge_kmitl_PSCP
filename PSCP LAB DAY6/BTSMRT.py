"""btsmrt"""
def main():
    """btsmrt"""
    day = str(input(""))
    age = float(input())
    hight = float(input())

    if day == "Children Day":
        if age <14 and hight <=140:
            print("FREE")
        else:
            print("PAY")
    elif day == "Senior Day":
        if age >=60 :
            print("FREE")
        elif age <14 and hight <90:
            print("FREE")
        else:
            print("PAY")
    elif day =="Normal Day":
        if age <14 and hight <90:
            print("FREE")
        else:
            print("PAY")

main()
