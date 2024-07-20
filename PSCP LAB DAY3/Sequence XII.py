"""Sequence XII"""
def back_side(num , can_up , counter) :
    """PEB-8 FIXED"""
    for _ in range(num - 1) :
        if can_up :
            if counter < num :
                counter += 1
                print(f"{counter:02d}" , end=" ")
            else :
                can_up = False
                counter -= 1
                print(f"{counter:02d}" , end= " ")
        else :
            counter -= 1
            print(f"{counter:02d}" , end=" ")

def down_side1(num) :
    """POSINGKI"""
    for row in range(2 , num+1) :
        canUp = True
        counter = row
        for _ in range(num) :
            if canUp :
                if counter < num :
                    print(f"{counter:02d}" , end=" ")
                    counter += 1
                else :
                    canUp = False
                    print(f"{counter:02d}" , end= " ")
            else :
                counter -= 1
                print(f"{counter:02d}" , end=" ")

        if counter == num :
            canUp = False
        else :
            canUp = True

        back_side(num , canUp , counter)
        print()

def main() :
    """Sequence XII"""
    num = int(input())
    for row in range(num , 0 , -1) :
        canUp = True
        counter = row
        for _ in range(num) :
            if canUp :
                if counter < num :
                    print(f"{counter:02d}" , end=" ")
                    counter += 1
                else :
                    canUp = False
                    print(f"{counter:02d}" , end= " ")
            else :
                counter -= 1
                print(f"{counter:02d}" , end=" ")

        if counter == num :
            canUp = False
        else :
            canUp = True

        back_side(num , canUp , counter)
        print()
    down_side1(num)
main()
