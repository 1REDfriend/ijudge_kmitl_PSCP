"""Password"""
import math
def check(text) :
    """Check password strength."""
    set1 = "abcdefghijklmnopqrstuvwxyz"
    set2 = set1.upper()
    set3 = "~`!@#$%^&*()_+=-{}[]|/\\\\:;\\\'\\\".?"
    set4 = "0123456789"

    num = 0

    if any(char in set1 for char in text) :
        num += 26

    if any(char in set2 for char in text) :
        num += 26

    if any(char in set3 for char in text) :
        num += 32

    if any(char in set4 for char in text) :
        num += 10

    num = math.log2(num**len(text))

    return num

def main() :
    """Password main"""
    passwd = input()
    result = int(check(passwd))

    print(result)
    if result >= 128 :
        print("Very Strong")
    elif result >= 60 :
        print("Strong")
    elif result >= 36 :
        print("Reasonable")
    elif result >= 28 :
        print("Weak")
    else :
        print("Very Weak")
main()
