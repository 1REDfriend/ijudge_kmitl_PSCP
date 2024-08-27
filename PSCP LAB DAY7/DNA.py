"""DNA"""
def find_dna(i1,i2 ,dna1 ,dna2) :
    """DNA Stories"""
    stack = ''
    minlen = min(len(dna1[i1:]) , len(dna2[i2:]))
    for i in range(1, minlen + 1) :
        if dna1[i1:i1+i] == dna2[i2:i2+i] :
            stack = dna1[i1:i1+i]
        else :
            stack = dna1[i1:i1+i-1]
            break
    return stack

def main() :
    """DNA main"""
    dna1 = input()
    dna2 = input()

    stackDNA = ''
    dnaResult = ''

    for i1,line1 in enumerate(dna1) :
        for i2,line2 in enumerate(dna2) :
            if line1 not in ("A" , "C" , "G" , "T") or line2 not in ("A" , "C" , "G" , "T") :
                dnaResult = "Error"
                break
            if line1 == line2 :
                stackDNA = find_dna(i1,i2 ,dna1 ,dna2)
                if len(stackDNA) > len(dnaResult) :
                    dnaResult = stackDNA

    if dnaResult :
        print(dnaResult)
    else :
        print("None")
main()
