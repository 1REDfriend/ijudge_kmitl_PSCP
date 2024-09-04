"""Shorten"""
def main() :
    """main"""
    last_num = int()
    first_st_num = int()
    result = str()

    while True :
        num = int(input())
        if num != -1 :
            if last_num + 1 == num :
                if not first_st_num :
                    first_st_num = last_num
            elif first_st_num :
                if result :
                    result += ', '
                if result.find(str(first_st_num)) != -1 :
                    result = result.replace(f', {first_st_num}', '')
                    result = result.replace(f'{first_st_num}, ', '')
                result += str(first_st_num)+"-"+str(last_num)+", "+str(num)
                first_st_num = int()
            else :
                if result :
                    result += ', '
                result += str(num)
            last_num = num
        else :
            if first_st_num :
                if result.find(str(first_st_num)) != -1 :
                    result = result.replace(f', {first_st_num}', '')
                if result :
                    result += ', '
                result += str(first_st_num)+"-"+str(last_num)
                first_st_num = int()
            elif num != -1 :
                if result :
                    result += ', '
                result += str(num)
            break
    print(result)
main()
