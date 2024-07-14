"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def uppers(num1 , num2 , num3) :
    """uppers"""
    sumnum1 = 0
    sumnum2 = 0
    sumnum3 = 0
    if num1 >= num2 and num1 >= num3 :
        sumnum1 = num1
    elif num2 >= num1 and num2 >= num3 :
        sumnum1 = num2
    elif num3 >= num1 and num3 >= num2 :
        sumnum1 = num3

    if sumnum1 == num1 :
        if num2 >= num3 :
            sumnum2 = num2
            sumnum3 = num3
        else :
            sumnum2 = num3
            sumnum3 = num2
    elif sumnum1 == num2 :
        if num1 >= num3 :
            sumnum2 = num1
            sumnum3 = num3
        else :
            sumnum2 = num3
            sumnum3 = num1
    elif sumnum1 == num3 :
        if num1 >= num2 :
            sumnum2 = num1
            sumnum3 = num2
        else :
            sumnum2 = num2
            sumnum3 = num1
    print(f"{sumnum1:.2f}, {sumnum2:.2f}, {sumnum3:.2f}")
def lowers(num1 , num2 , num3):
    """lower"""
    sumnum1 = 0
    sumnum2 = 0
    sumnum3 = 0
    if num1 <= num2 and num1 <= num3 :
        sumnum1 = num1
    elif num2 <= num1 and num2 <= num3 :
        sumnum1 = num2
    elif num3 <= num1 and num3 <= num2 :
        sumnum1 = num3

    if sumnum1 == num1 :
        if num2 <= num3 :
            sumnum2 = num2
            sumnum3 = num3
        else :
            sumnum2 = num3
            sumnum3 = num2
    elif sumnum1 == num2 :
        if num1 <= num3 :
            sumnum2 = num1
            sumnum3 = num3
        else :
            sumnum2 = num3
            sumnum3 = num1
    elif sumnum1 == num3 :
        if num1 <= num2 :
            sumnum2 = num1
            sumnum3 = num2
        else :
            sumnum2 = num2
            sumnum3 = num1
    print(f"{sumnum1:.2f}, {sumnum2:.2f}, {sumnum3:.2f}")
def main() :
    """def"""
    text = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    if text == "Ascend" :
        lowers(num1 , num2 , num3)
    else :
        uppers(num1 , num2 , num3)
main()
