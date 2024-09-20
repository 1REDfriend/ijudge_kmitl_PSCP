"""isprime_small"""
def main():
    """_"""
    x=int(input())
    n=0
    for i in range(2,x+1):
        g=False
        for y in range(2,i):
            if not i % y :
                g = True
        if not g :
            n+=1
    print(n)
main()
