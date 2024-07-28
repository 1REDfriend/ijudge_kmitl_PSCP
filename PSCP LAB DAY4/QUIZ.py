def main() :
    couter = 1
    num = int(input())
    while couter <= num :
        if couter % 15 == 0 :
            print("FizzBuzz")
        elif couter % 5 == 0 :
            print("Buzz")
        elif couter % 3 == 0 :
            print("Fizz")
        else :
            print(couter)
        couter += 1
main()
