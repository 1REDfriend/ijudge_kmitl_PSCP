"""Netflix"""
def endOfNetflix(m,b,s,p,price) :
    """if else lastest"""
    if s > 1 :
        p += 1
        s -= 1
        price = price + (349 - 419)
    if p :
        print(f'Premium x {p}')
    elif s :
        print(f'Standard x {s}')
    elif b :
        print(f'Basic x {b}')
    elif m :
        print(f'Mobile x {m}')
    print(f'Total = {price} THB')
def whyloop(n1,n2 ,n3) :
    """while loop"""
    counter = 0
    while (n1 > 0 or n2 > 0) :
        counter += 1
        n1 -= n3
        n2 -= n3
    return counter
def zeroTrush(n) :
    """not minus"""
    if n > 0 :
        return 0
    return n

def main() :
    """Netflix main"""
    nOfScreen = int(input())
    nOfPhone = int(input())
    input()
    watchOnMobile = input()
    watchOnLaptop = input()
    hd = input()
    ultraHD = input()

    m = 0
    b = 0
    s = 0
    p = 0
    totalPrice = 0

    if ultraHD == "Yes" :
        p += 1
        nOfPhone = zeroTrush(nOfPhone - 4)
        nOfScreen = zeroTrush(nOfScreen - 4)
        p += whyloop(nOfPhone , nOfScreen , 4 )
        totalPrice += p*419
    elif hd == "Yes" :
        s += 1
        nOfPhone = zeroTrush(nOfPhone - 2)
        nOfScreen = zeroTrush(nOfScreen - 2)
        s += whyloop(nOfPhone , nOfScreen , 2 )
        totalPrice += s*349
    elif watchOnLaptop == "Yes" :
        b += 1
        nOfPhone = zeroTrush(nOfPhone - 1)
        nOfScreen = zeroTrush(nOfScreen - 1)
        b += whyloop(nOfPhone , nOfScreen , 1 )
        totalPrice += b*279
    elif watchOnMobile == 'Yes' :
        m += 1
        nOfPhone = zeroTrush(nOfPhone - 1)
        nOfScreen = zeroTrush(nOfScreen - 1)
        m += whyloop(nOfPhone , nOfScreen , 1 )
        totalPrice += m*99
    else :
        while (nOfPhone > 0 or nOfScreen > 0) :
            m += 1
            totalPrice += 99
            nOfPhone = zeroTrush(nOfPhone - 1)
            nOfScreen = zeroTrush(nOfScreen - 1)
    endOfNetflix(m,b,s,p,totalPrice)
main()