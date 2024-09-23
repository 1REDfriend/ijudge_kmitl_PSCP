"""PickThemAgain"""
def main() :
    """PickThemAgain main"""
    text_split = sorted(input().split(" "), key=lambda x : x.isnumeric(), reverse=True)
    hsa_been = False
    for i in text_split :
        if i.isnumeric() :
            if not int(i) % 3 or not int(i) % 5 :
                print(i)
                has_been = True
    if not has_been :
        print("Nope")
main()
