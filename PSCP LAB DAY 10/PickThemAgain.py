"""PickThemAgain"""
def main() :
    """PickThemAgain main"""
    text_split = input().split(" ")
    hsa_been = False
    for i in text_split :
        if i.isnumeric() :
            if not i % 3 or not i % 5 :
                print(i)
                has_been = True
    if not has_been :
        print("Nope")
main()
