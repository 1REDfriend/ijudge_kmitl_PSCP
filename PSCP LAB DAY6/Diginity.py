"""Diginity"""
def auto(number) :
    """loop sum value"""
    result = 0
    for i in number:
        result += int(i)
    if len(str(result)) > 1 :
        return auto(str(result))
    return result
def main() :
    """Diginity main"""
    while True :
        number = input()
        if number == "0" :
            break
        print(auto(number))
main()
