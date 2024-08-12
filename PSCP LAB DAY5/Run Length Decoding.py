"""Run Length Decoding"""
def main() :
    """Run Length Decoding main"""
    code = input()
    lastNumber = ''
    result = ''
    for i in code :
        if i.isdigit() :
            lastNumber += i
        else :
            result += i*int(lastNumber)
            lastNumber = ''
    print(result)
main()
