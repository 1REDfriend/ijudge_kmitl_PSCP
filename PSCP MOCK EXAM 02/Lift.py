"""Lift"""
def main() :
    """Lift main"""
    person = int(input())
    moxWeight = float(input())
    child = 0
    oldchild = 0
    liftWeight = 0
    for _ in range(person) :
        age = int(input())
        weight = float(input())
        if age < 12 :
            child += 1
        else :
            oldchild += 1
        liftWeight += weight
    if child and oldchild and liftWeight <= moxWeight:
        print("Safe")
    elif child and not oldchild :
        print("Not Safe")
    elif liftWeight > moxWeight :
        print("Not Safe")
    else :
        print("Safe")
main()
