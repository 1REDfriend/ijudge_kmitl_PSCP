"""Matrix_MN"""
def main() :
    """Matrix_MN main"""
    m = int(input())
    n = int(input())
    result = ''
    for i in range(m*n) :
        num = input().strip()
        if not i % n and i:
            result = result.strip() + "\n"
        result += f"{num} "
    print(result)
main()
