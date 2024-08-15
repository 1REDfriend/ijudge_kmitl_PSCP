"""WeightStation"""
def main() :
    """WeightStation"""
    averge = float(input())
    wheel1 = float(input())
    wheel2 = float(input())
    wheel3 = float(input())

    allWeight =  wheel1+wheel2+wheel3
    brokenWheel = (averge*4 )-allWeight
    if allWeight + brokenWheel <= 15000 :
        balance = averge / 2
        result = ""
        if not balance <= brokenWheel <= averge + balance :
            result = "Unbalance"
        if not balance <= wheel1 <= averge + balance :
            result = "Unbalance"
        if not balance <= wheel2 <= averge + balance :
            result = "Unbalance"
        if not balance <= wheel3 <= averge + balance :
            result = "Unbalance"
        if result :
            print(result)
        else :
            print(f"Pass {brokenWheel:.2f}")
    else :
        print("Overweight")
main()
