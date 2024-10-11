"""LineSorting"""
def main() :
    """LineSorting main"""

    count = int(input())
    text_list = []

    for i in range(count) :
        text_list.append(input())

    text_list.sort(key=len)
    for i in text_list :
        print(i)
main()
