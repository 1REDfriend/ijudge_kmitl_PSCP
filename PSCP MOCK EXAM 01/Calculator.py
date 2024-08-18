"""Calculator"""
def main() :
    """Calculator main"""
    needNum = int(input())
    result = 1
    if needNum > 1 :
        for i in range(1,needNum+1) :
            for _ in range(len(str(i))) :
                result += 1
            if i > 1 :
                result += 1
    print(result)
main()
