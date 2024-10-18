"""Diamond I"""
def main() :
    """Diamond I main"""
    deep = int(input())
    wide = int(input())

    lt = [0 for _ in range(wide)]

    for _ in range(deep):
        unya_manee = input().strip().split(" ")
        for i in range(wide) :
            lt[i] += int(unya_manee[i])
    lt.sort(reverse=True)
    print(lt[0])
main()
