"""WordSequence I"""
def main() :
    """WordSequence I main"""
    txt = input()
    for i in range(len(txt)) :
        print(txt[:i+1])
main()
