"""PickThemAgain"""
def main() :
    """PickThemAgain main"""
    text = input().split(" ")
    text_split = text
    text_split.reverse()
    has_been = False
    for i in text_split :
        if not int(i) % 3 or not int(i) % 5 :
            print(i)
            has_been = True
    if not has_been :
        print("Nope")
main()
