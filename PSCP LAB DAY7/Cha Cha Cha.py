"""Cha Cha Cha"""
import math
def main() :
    """Cha Cha Cha main"""
    dayCount = int(input())
    result = 0
    for _ in range(dayCount) :
        hour = math.ceil(float(input()))
        result += hour * 8720
    print(result)
main()
