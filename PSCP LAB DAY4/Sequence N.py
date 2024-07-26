"""Sequence N"""
def main() :
    """main"""
    num = int(input())
    print(f"*{' '*(num-2)}*")
    for i in range(num-2) :
        print(f"*{' '*i}*{' '*(num-3-i)}*")
    print(f"*{' '*(num-2)}*")
main()
