'''g'''
def main():
    '''g'''
    n = int(input())
    l = []
    m = 0
    for _ in range(n):
        t = input().split()
        m += float(t[1])
        l.append(t)
    m /= n
    l = sorted(l,key=lambda x: float(x[1]))
    for i,v in enumerate(l) :
        if float(v[1]) >= m:
            print(f'{l[i-1][0]}\t{l[i-1][1]}')
            break
main()
