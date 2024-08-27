"""Shorten"""
def main() :
    """Shorten main"""

    stack = ''
    result = ''
    last_result = ''

    count = 0
    check_num = 0
    first = 0
    num = -1

    firstTime = True
    hasStack = False

    while True :
        if num > -1 :
            result += ", "
        num = int(input())
        if num != -1 :
            if count > 0 :
                if check_num+1 == num :
                    if firstTime :
                        first = check_num
                        firstTime = False
                    stack = f'{first}-{num}'
                    hasStack = True
                    check_num = num
                else :
                    firstTime = True
                    if count == 1 :
                        result += check_num
                    if stack :
                        if hasStack :
                            result = last_result + stack 
                        else :
                            result += stack + ", " + str(num) 
                            stack = ''
                    else :
                        last_result = result
                        result += str(num)
                    check_num = num
            else :
                check_num = num
            count += 1
        else :
            break
    if stack :
        result += stack
    print(result)
main()
