"""WeightStation"""
def main() :
    """WeightStation"""
    wheel1 = float(input())
    wheel2 = float(input())
    wheel3 = float(input())
    wheel4 = float(input())

    sumweight =  wheel2 + wheel3 + wheel4
    brokenweight = (wheel1 * 4 ) - sumweight
    if sumweight + brokenweight <= 15000 :
        balance = wheel1 / 2
        ans = ""
        if not balance <= brokenweight <= wheel1 + balance :
            ans = "Unbalance"
        if not balance <= wheel2 <= wheel1 + balance :
            ans = "Unbalance"
        if not balance <= wheel3 <= wheel1 + balance :
            ans = "Unbalance"
        if not balance <= wheel4 <= wheel1 + balance :
            ans = "Unbalance"
        if ans :
            print(ans)
        else :
            print(f"Pass {brokenweight:.2f}")
    else :
        print("Overweight")
main()
