"""Triangle I"""
def find_mox(num1 , num2 , num3 ) :
    """max"""
    if num1 >= num2 and num1 >= num3 :
        return [num1 , 1]
    if num2 >= num1 and num2 >= num3 :
        return [num2 , 2]
    return [num3 , 3]
def main() :
    """Triangle I"""
    wood1 = float(input())
    wood2 = float(input())
    wood3 = float(input())

    c = find_mox(wood1 , wood2 , wood3)
    sumx = 0
    match c[1] :
        case 1 :
            sumx = wood2**2 + wood3**2
        case 2 :
            sumx = wood3**2 + wood1**2
        case 3 :
            sumx = wood1**2 + wood2**2

    c = c[0]**2
    if sumx - 0.01 <= c <= sumx + 0.01 :
        print("Yes")
    else :
        print("No")
main()
