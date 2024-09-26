"""US Interstate Number System"""
def main() :
    """US Interstate Number System main"""
    road = input()

    if len(road) <= 2 and int(road):
        if road[-1] == "0" :
            print("Horizontal Major Interstate")
            print(f"I-{int(road)}")
        elif road[-1] == "5" :
            print("Vertical Major Interstate")
            print(f"I-{int(road)}")
        else :
            print("Others")
    elif len(road) == 3 and int(road[1:]):
        if not int(road[0]) % 2 and road[-1] in ("5","0"):
            print("Even Minor Interstate")
            print(f"I-{int(road[1:])}")
        elif road[-1] in ("5","0"):
            print("Odd Minor Interstate")
            print(f"I-{int(road[1:])}")
        else :
            print("Others")
    else :
        print("Others")
main()
