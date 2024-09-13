'''h'''
import math
def main():
    '''f'''
    n = int(input())
    l = []
    f = 0
    r = 0
    result = 0
    for _ in range(n):
        l.append(float(input()))
    l.sort()
    if not n % 2 :
        first = l[n//2]
        end = l[(n//2) + 1]
        f = (first+end)/2
        r = (f+1)/2
        first = l[math.floor(r)]
        end = l[math.floor(r) + 1]
        result = (first+end)/2
    else :
        result = l[int((l[((n//2))]+1)/2)]
    print(f'{result:.3f}')
main()
