"""Future Message"""
def main():
    """Future Message"""
    x = input()
    if x.isdigit():
        print("Number")
    elif x.islower():
        print("Lowercase")
    elif x.isupper():
        print("Uppercase")
    elif x.isspace():
        print("Space")
    elif x.istitle():
        print("Title")
    else:
        print("Other")
main()
