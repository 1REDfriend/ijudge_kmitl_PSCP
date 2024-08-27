"""Home Run"""
def main() :
    """Home Run main"""
    count = int(input())
    canTab = float(input())
    result = 0
    for _ in range(count) :
        if canTab > float(input()) :
            result += 1
    print(result)
main()
