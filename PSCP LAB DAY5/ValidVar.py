"""ValidVar"""
def main() :
    """ValidVar main"""
    count = int(input())
    specialString = """abcdefghijklmnopqrstuvwxyzABCDEFCHIJKLMNOPQRSTUVWXYZ_
1234567890"""
    keywords = {
        'if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break',
        'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None'
    }
    for _ in range(count) :
        passwd = input().strip()
        isBreak = False
        for i,v in enumerate(passwd) :
            if v not in specialString :
                print('Invalid')
                isBreak = True
                break
            if v.isspace() :
                print("Invalid")
                isBreak = True
                break
            if not i and v.isnumeric() :
                print("Invalid")
                isBreak = True
                break
            if passwd in keywords :
                print("Invalid")
                isBreak = True
                break
        if not isBreak :
            print("Valid")
main()
