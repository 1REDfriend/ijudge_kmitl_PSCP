"""LastStand"""
def main() :
    """LastStand"""
    text_list = input().replace("[","").replace("]","")
    text_list = text_list.split(",")

    for i in text_list :
        print(i[-1])
main()
