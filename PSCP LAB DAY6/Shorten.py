"""Shorten"""
def main() :
    """Shorten main"""
    result = ''
    stack = ''

    first = 0
    last = -2
    count = 0

    while True :
        num = int(input())
        if num != -1 :
            if last + 1 == num :
                stack = f'{first}-{num}'
            else :
                first = num
                if stack :
                    result += stack + ', '
                    stack = ''
                elif count > 0 :
                    result += str(num) + ', '
            last = num
        else :
            break
        count += 1
    print(result)
main()
