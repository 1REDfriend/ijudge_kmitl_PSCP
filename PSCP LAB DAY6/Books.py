"""Books"""
import math
def main() :
    """Books main"""
    books = int(input())
    page = int(input())
    x = int(input())
    y = int(input())

    dayCount = 0
    readDayCount = 0
    lastDayRead = 0

    pageTemp = page

    while books > 0 :
        pageTemp -= math.ceil((x+lastDayRead+dayCount)/(y+lastDayRead+dayCount))
        dayCount += 1
        readDayCount += 1
        if pageTemp <= 0 :
            books -= 1
            pageTemp = page
            lastDayRead = readDayCount
    print(dayCount)
main()
