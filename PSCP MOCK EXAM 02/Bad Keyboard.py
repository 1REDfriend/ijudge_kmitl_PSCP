"""Bad Keyboard"""
def main() :
    """Bad Keyboard main"""
    text = input()
    result = ''
    for i in text :
        if i == "i" :
            result += "o"
        elif i == "o" :
            result += 'i'
        elif i == "I" :
            result += "O"
        elif i == "O" :
            result += 'I'
        else :
            result += i
    print(result)
main()
