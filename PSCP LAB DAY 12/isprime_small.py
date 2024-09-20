"""isprime_small"""
def main():
    """_"""
    x=int(input())
    y="Yes"
    for i in range(2,x):
        if not x % i :
            y="No"
    if not x or x==1:
        y="No"
    print(y)
main()
