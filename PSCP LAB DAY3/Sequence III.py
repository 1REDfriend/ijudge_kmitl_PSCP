"""Sequence III"""
def main() :
    """Sequence III"""
    num=int(input())
    var=2
    for _ in range(num) :
        for i in range(var,num+var):
            print(i,end=" ")
        print()
        var += 1
main()
