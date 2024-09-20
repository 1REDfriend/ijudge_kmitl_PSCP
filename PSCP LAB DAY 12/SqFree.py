"""isprime_small"""
def main():
    """_"""
    n=int(input())
    nn=0
    for i in range(2,n+1):
        if i**2 <= n :
            if n%(i**2):
                nn+=1
        else :
            break
    print(nn)
main()
