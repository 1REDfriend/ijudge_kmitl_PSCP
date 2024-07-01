"""Hamberger"""
def main() :
    """Def"""
    left = int(input())
    right = int(input())
    pig = int((left + right) * 2)
    star = "*" * pig
    leftberge = "|" * left
    rightberge = "|" * right
    print(f"{leftberge}{star}{rightberge}")
main()
