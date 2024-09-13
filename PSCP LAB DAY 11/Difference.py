"""Difference"""
def main():
    """Difffffff"""
    a = int(input())
    b = int(input())
    a_dist = {}
    b_dist = {}
    for _ in range(a):
        set_1 = input()
        if a_dist.get(set_1) is None :
            a_dist.update({set_1 : 0})
    for _ in range(b) :
        set_2 = input()
        if b_dist.get(set_2) is None :
            b_dist.update({set_2 : 0})
    for x,b in b_dist.items() :
        if x in sorted(a_dist) :
            a_dist.pop(x)
    a_dist = sorted(a_dist, key=int , reverse=False)
    for i in a_dist :
        print(i, end=" ")
main()
