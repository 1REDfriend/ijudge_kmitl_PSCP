"""Elo"""
def main() :
    """Elo MAIN"""
    num1 = int(input())
    num2 = int(input())
    text = input()
    result = 0
    if text == "A" :
        result = 1/(1+(10**((num2-num1)/400)))
    elif text == "B" :
        result = 1/(1+(10**((num1-num2)/400)))
    print(f"{result:.2f}")
main()
