"""HowLong"""
def main() :
    """AMin"""
    num = input()
    bout = 0
    if int(num) == abs(int(num)) :
        for _ in num :
            bout += 1
    else :
        for _ in num:
            bout += 1
        bout -= 1
    print(bout)
main()
