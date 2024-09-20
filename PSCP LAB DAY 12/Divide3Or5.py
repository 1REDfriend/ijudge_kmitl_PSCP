"""isprime_small"""
def main():
    """_"""
    n=int(float(input()))
    sumn=0
    for i in range(1,n+1):
        if not i%3 or not i%5:
            sumn+=i
    print(sumn)
main()
