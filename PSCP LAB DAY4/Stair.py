"Stair"
def main():
    "Stair main"
    canHigh = int(input())
    stairStep = int(input())
    currentStep = 0
    count = 0
    for _ in range(stairStep):
        height = int(input())
        if height > canHigh:
            print("NO")
            return
        currentStep += height
        if currentStep >= canHigh:
            count += 1
            if currentStep == canHigh:
                currentStep = 0
            elif currentStep > canHigh:
                currentStep -= currentStep - height
        if currentStep > canHigh:
            print("NO")

    if currentStep > 0:
        count += 1
    if not canHigh:
        count = 0
    print(count)

main()
