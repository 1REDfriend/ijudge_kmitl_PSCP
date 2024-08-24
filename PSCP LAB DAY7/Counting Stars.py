"""Counting Stars"""
def main() :
    """Counting Stars main"""
    star = input()
    stack = ''
    constellation = 0
    comet = 0
    shooting_star = 0
    for i in star :
        if i != " " :
            stack += i
        else :
            if stack[1]+stack[0] == "~*" or stack == "~*":
                comet += 1
            elif stack[1]+stack[0] == "/*" or stack == "/*":
                shooting_star += 1
            elif stack == "**":
                constellation += 1
            stack = ""
    if constellation or comet or shooting_star :
        print(f'constellation: {constellation}')
        print(f'comet: {comet}')
        print(f'shooting star: {shooting_star}')
    else :
        print("Tonight is a quiet night.")
main()
