"""isprime_small"""
def main():
    """_"""
    num1=int(input())
    num2=int(input())
    num_min = min(num1,num2)
    for i in range(num_min,0,-1):
        if not num1%i and not num2%i:
            print(i)
            break
    if not num_min :
        print(max(num1,num2))
main()
