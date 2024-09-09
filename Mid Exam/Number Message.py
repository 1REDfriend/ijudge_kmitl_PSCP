"""Number Message"""
def check_again(stack) :
    """def"""
    result = ''
    if stack == "1" :
        result += "I"
    elif stack == "3" :
        result += "E"
    elif stack == "4" :
        result += "A"
    elif stack == "5" :
        result += "S"
    elif stack == "0" :
        result += "O"
    elif stack == "12" :
        result += "R"
    elif stack == "13" :
        result += "B"
    return result
def main() :
    """Number Message main"""
    text = input().upper()
    result = ''
    stack = ''
    stackmore = False
    for i in range(len(text)) :
        if text[i].isnumeric() and stack.startswith("1") :
            stack += text[i]
            stackmore = True
            if stack.startswith("1") :
                if stack[1:] != "2" and stack[1:] != "3"  :
                    result += check_again(stack[0])
                    stack = stack[1:]
        elif text[i].isnumeric() :
            stack = text[i]
            stackmore = True
            if stack.startswith("1") :
                stackmore = False
        if stackmore or text[i].isalpha() or text[i] == " " or i >= len(text)-1:
            if stack :
                result += check_again(stack)
                stack = ''
            if text[i].isalpha() or text[i] == " ":
                result += text[i]
            stackmore = False
    print(result)
main()
