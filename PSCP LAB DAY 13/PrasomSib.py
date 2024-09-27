'''PrasomSib'''
def main():
    '''Smth'''
    x = str(input())
    sums = 0
    counter = 0
    for i, char in enumerate(x) :
        sums = int(char)
        for char2 in x[i+1:] :
            sums += int(char2)
            if sums == 10 :
                counter += 1
                break
            if sums > 10 :
                break
    print(counter)
main()
