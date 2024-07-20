""""Sequence XI"""
def down_sequence(num) :
    """down"""
    for i in range(num-1 , 0 , -1) :
        counter = 1
        bern = -2
        for _ in range(num) :
            if counter < i :
                print(f"{counter:02d}" , end=" ")
                counter += 1
            else :
                print(f"{counter:02d}" , end=" ")
                bern += 1
        for _ in range(num-1) :
            if counter > 1 > bern:
                print(f"{counter:02d}" , end=" ")
                counter -= 1
            else :
                print(f"{counter:02d}" , end=" ")
                bern -= 1
        print()
def main() :
    """Sequence XI"""
    num = int(input())
    for i in range(1 , num + 1) :
        counter = 1
        bern = -2
        for _ in range(num) :
            if counter < i :
                print(f"{counter:02d}" , end=" ")
                counter += 1
            else :
                print(f"{counter:02d}" , end=" ")
                bern += 1
        for _ in range(num-1) :
            if counter == num :
                counter -= 1
            if counter > 1 > bern :
                print(f"{counter:02d}" , end=" ")
                counter -= 1
            else :
                print(f"{counter:02d}" , end=" ")
                bern -= 1
        print()
    down_sequence(num)
main()
