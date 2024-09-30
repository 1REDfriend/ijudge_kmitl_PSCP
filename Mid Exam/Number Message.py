"""Number Message"""
def main() :
    """Number Message"""
    text = input()
    text = text.replace("13","B")
    text = text.replace("12","R")
    text = text.replace("0","O")
    text = text.replace("5","S")
    text = text.replace("4","A")
    text = text.replace("3","E")
    text = text.replace("1","I")
    for char in "26789":
        text = text.replace(char, "")
    print(text.upper())
main()
