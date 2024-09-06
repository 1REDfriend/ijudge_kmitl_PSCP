"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main() :
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain main"""
    text = input().split(" ")
    text_list = []
    for i in text :
        if len(i) > 2 :
            text_list.append(i.rstrip("."))
    text_list.sort()
    for i in text_list :
        print(i)
main()
