"""Real"""
def check(value) :
    count = 0
    value = str(value)
    for i in value :
        if i.isnumeric() :
            count += 1
    if count < 3 :
        return "Error"
    return f'{float(value):.2f}'
def main() :
    """Real main"""
    result = ''
    for _ in range(3) :
        a = input()
        b = input()
        c = input()
        d = input()
        e = input()
        f = input()
        g = input()
        db = input()
        if b=="on"and c=="on"and "off"==a and "off"==d and "off" == e and "off" == f and "off" ==g:
            result += "0"
        elif "on" == a and "on" == b and "on" == c and"off"==d and"off"==e and"off"==f and"off"==g:
            result += "7"
        elif "on" == b and "on" == c and "on" == g and"on"==f and"off"==a and"off"==d and"off"== e:
            result += "4"
        elif "on" == a and "on" == b and "on" == c and"on"==d and"on"==g and"off"==e and"off"==f:
            result += "3"
        elif "on" == a and "on" == b and "on" == d and"on"==e and"on"==g and"off"== c and"off"==f:
            result += "2"
        elif "on" == a and "on" == c and "on" == d and"on"==f and"on"==g and"off"==b and"off"==e:
            result += "5"
        elif "on" == a and "on" == b and "on" == c and "on" == d and"on"==f and"on"==g and"off"==e:
            result += "9"
        elif "on" == a and "on" == c and "on" == d and"on"==e and"on"==f and"on"==g and"off"==b:
            result += "6"
        elif "on" == a and "on" == b and "on" == c and"on"==d and"on"==e and"on"==f and"off"==g:
            result += "0"
        elif "on" == a and "on" == b and "on" == c and"on"==d and"on"==e and"on"==f and"on"==g:
            result += "8"
        if db == "on" :
            result += "."
    print(check(result))
main()
