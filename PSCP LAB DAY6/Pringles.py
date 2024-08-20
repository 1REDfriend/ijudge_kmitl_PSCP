"""Pringles"""
def main() :
    """Pringles main"""
    box = input()
    lay = input()
    input()
    eat = int(input())

    count = 0
    eatLay = 0
    layAlive = 0

    for i in lay :
        if count >= eat :
            break
        if i == ")" :
            eatLay += 1
        count += 1

    lay = " "*(count)+lay[eat:]
    for i in lay :
        if i == ")" :
            layAlive += 1

    if layAlive > 0 :
        print(eatLay)
        print("There are still some left.")
    else :
        print(eatLay)
        print("None.")
    print(box)
    print(lay)
    print(box)
main()
