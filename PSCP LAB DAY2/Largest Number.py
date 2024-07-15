"""Largest Number"""
def find_mox(num1 , num2 , num3 ) :
    """max"""
    if num1 >= num2 and num1 >= num3 :
        return [num1 , 1]
    if num2 >= num1 and num2 >= num3 :
        return [num2 , 2]
    return [num3 , 3]
def main() :
    """Largest Number"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    mox1 = find_mox(num1 , num2 , num3)
    mox2 = 0
    mox3 = 0
    match mox1[1] :
        case 1 :
            if num2 >= num3 :
                mox2 = num2
                mox3 = num3
            else :
                mox2 = num3
                mox3 = num2
        case 2 :
            if num1 >= num3 :
                mox2 = num1
                mox3 = num3
            else :
                mox2 = num3
                mox3 = num1
        case 3 :
            if num1 >= num2 :
                mox2 = num1
                mox3 = num2
            else :
                mox2 = num2
                mox3 = num1
    mox1 = str(mox1[0])
    mox2 = str(mox2)
    mox3 = str(mox3)
    print(mox1+mox2+mox3)
main()
