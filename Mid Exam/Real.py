"""Real"""
def check(value):
    """Real check"""
    count = 0
    value = str(value)
    for i in value:
        if i.isnumeric():
            count += 1
    if count < 3 or value.count(".") >= 2:
        return "Error"
    return f'{float(value):.2f}'

def main():
    """Real main"""
    result = ''
    for _ in range(3):
        a = input()
        b = input()
        c = input()
        d = input()
        e = input()
        f = input()
        g = input()
        db = input()

        if b == "on" and c == "on" and all(x == "off" for x in [a, d, e, f, g]):
            result += "1"
        if all(x == "on" for x in [a, b, c]) and all(x == "off" for x in [d, e, f, g]):
            result += "7"
        if all(x == "on" for x in [b, c, f, g]) and all(x == "off" for x in [a, d, e]):
            result += "4"
        if all(x == "on" for x in [a, b, c, d, g]) and all(x == "off" for x in [e, f]):
            result += "3"
        if all(x == "on" for x in [a, b, d, e, g]) and all(x == "off" for x in [c, f]):
            result += "2"
        if all(x == "on" for x in [a, c, d, f, g]) and all(x == "off" for x in [b, e]):
            result += "5"
        if all(x == "on" for x in [a, b, c, d, f, g]) and e == "off":
            result += "9"
        if all(x == "on" for x in [a, c, d, e, f, g]) and b == "off":
            result += "6"
        if all(x == "on" for x in [a, b, c, d, e, f]) and g == "off":
            result += "0"
        if all(x == "on" for x in [a, b, c, d, e, f, g]):
            result += "8"

        if db == "on":
            result += "."

    print(check(result))

main()
