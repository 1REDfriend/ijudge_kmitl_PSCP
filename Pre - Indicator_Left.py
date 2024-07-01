"""Indicator_Left"""
def main() :
    """def"""
    num = int(input())
    height = int(input())
    star = "*" * num
    prompt = "DOWN"
    temp = 0
    if height == 1 :
        print(star)
    for i in range(height-1) :
        if prompt == "DOWN" :
            space = " " * (((height)//2) - i)
            print(f"{space}{star}")
            if i+1 >= ((height)//2) :
                prompt = "UP"
                temp = i
                print(star)
        elif prompt == "UP" :
            space = " " * (i - temp)
            print(f"{space}{star}")
main()
