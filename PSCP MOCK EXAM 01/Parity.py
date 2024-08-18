"""Parity"""
def main() :
    """Parity main"""
    sevenBit = input()
    parity = input()
    count = 0
    for i in sevenBit :
        if i == "1" :
            count += 1
    if parity == "Even" :
        sevenBit += str(count%2)
    elif parity == "Odd" :
        if not count%2 :
            sevenBit += "1"
        else :
            sevenBit += "0"
    print(sevenBit)
main()
