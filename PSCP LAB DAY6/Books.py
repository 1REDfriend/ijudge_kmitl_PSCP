"""Books"""
import math

def main() :
    """Books main"""
    books = int(input())
    page = int(input())
    x = int(input())
    y = int(input())

    pageTemp = page
    dayCount = 0

    while books > 0 :
        pageTemp -= math.ceil(((x+dayCount)/(y+dayCount))*page)
        if math.ceil(((x+dayCount)/(y+dayCount))*page) >= page:
            break
        if pageTemp <= 0 :
            pageTemp = page
            books -= 1
        dayCount += 1
    print(dayCount + books)
main()
