'''gm'''
def main():
    '''ejfbukjegfujewhgew'''
    x=int(input())
    y=int(input())
    val=0
    print("pass : ",end="")
    if x==y and not x%2 and not y%2:
        print(x,end="")
        val=x
    elif x>y:
        if x%2 == 1:
            for i in range (x-1,y-1,-2):
                print(i,end=" ")
                val+=i
        elif not x%2:
            for i in range (x,y-1,-2):
                print(i,end=" ")
                val+=i
    elif x<y:
        if x%2 == 1:
            for i in range (x+1,y+1,2):
                print(i,end=" ")
                val+=i
        elif not x%2:
            for i in range (x,y+1,2):
                print(i,end=" ")
                val+=i
    print()
    print("Sum :",val)
main()
