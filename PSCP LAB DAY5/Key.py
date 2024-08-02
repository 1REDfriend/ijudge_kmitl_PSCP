"""Key"""
def main():
    """Key"""
    num = input()
    sumNum = 0
    multiplyNum = 0
    for i in num :
        sumNum += int(i)
    multiplyNum = int(num[-3:]) * 10
    key = sumNum + multiplyNum
    if key < 1000 :
        key += 1000
    key = str(key)
    key = key[-4:]
    key = int(key)
    print(f"{key:04d}")
main()
