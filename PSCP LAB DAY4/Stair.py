"""Stair"""
def main() :
    """main of Stair"""
    canStepping = int(input())
    stepStair = int(input())

    cat_stair = []
    stack_step = 0

    result = 0
    if stepStair <= 0 :
        result = 0
    else :
        for _ in range(stepStair) :
            cat_stair.append(int(input()))
        for v in cat_stair :
            if v <= canStepping :
                if stack_step >= canStepping :
                    result += 1
                    stack_step = 0
                stack_step += v
            else :
                result = -1
                break
    if stack_step > 0 :
        result += 1
        stack_step = 0
    if result < 0 :
        print("No")
    else :
        print(result)
main()
