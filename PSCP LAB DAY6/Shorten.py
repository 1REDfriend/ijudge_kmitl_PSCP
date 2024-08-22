"""Shorten"""
def main() :
    """Shorten main"""
    result = ''
    stack = ''

    first = 0
    last = -1

    while True :
        num = int(input())
        if num > -1 :
            if num == last + 1 :
                stack = f'{first}-{num}'
                last = num
            else :
                first = num
                if stack :
                    result = result[:(-1-(len(str(first))))]
                    result += stack + ", " 
                    result += str(num) + ', '
                    stack = ''
                elif last > -1 :
                    result += str(num) + ", "
                last = num
        if num <= -1 :
            if stack :
                result = result[:(-2-(len(str(first))))]
                result += stack + ", " 
                stack = ''
            result = result[:-2]
            break
    print(result)
main()
