"""Kaprekar use bubble"""
def mox(num):
    """Find more than value"""
    num = list(num)  # Convert string to list of characters
    n = len(num)
    for _ in range(n):
        for i in range(n - 1):
            if int(num[i]) < int(num[i + 1]):
                num[i], num[i + 1] = num[i + 1], num[i]
    return int(''.join(num))

def mon(num):
    """Find less than value"""
    num = list(num)  # Convert string to list of characters
    n = len(num)
    for _ in range(n):
        for i in range(n - 1):
            if int(num[i]) > int(num[i + 1]):
                num[i], num[i + 1] = num[i + 1], num[i]
    return int(''.join(num))

def main():
    """Kaprekar main"""
    number = input().zfill(4)  # Ensure 4-digit input
    result = 0
    count = 0
    while result != 6174:
        if count > 0:
            number = str(result).zfill(4)  # Ensure 4-digit number
        moreNum = mox(number)
        lessNum = mon(number)
        result = moreNum - lessNum
        count += 1
    print(count)

main()
