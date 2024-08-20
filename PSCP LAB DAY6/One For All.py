"""One For All"""
def main() :
    """One For All main"""
    num = int(input())
    result = ''
    for i in range(1 , num+1) :
        name = input()
        if i >= num :
            result += name
        elif not i % 2 :
            result += f'{name}{"-"*i}'
        elif i % 2 :
            result += f'{name}{"*"*i}'
    if num <= 0 :
        print()
    else :
        result += f'_{num}'
        print(result)
main()
