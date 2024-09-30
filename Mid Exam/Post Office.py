"""Post Office"""
def en(envelop) :
    """en"""
    en_result = 0
    for _ in range(envelop) :
        weight = float(input())
        if 1000 < weight <= 2000 :
            en_result += 68
        elif weight > 500 :
            en_result += 48
        elif weight > 250 :
            en_result += 33
        elif weight > 100 :
            en_result += 28
        elif weight > 20 :
            en_result += 23
        elif weight > 10 :
            en_result += 18
        elif weight >= 0 :
            en_result += 16
        en_result += 13
    return en_result
def pc(package) :
    """pc"""
    pc_result = 0
    for _ in range(package) :
        weight = float(input())
        if 1000 < weight <= 2000:
            pc_result += 70
        elif weight > 500 :
            pc_result += 55
        elif weight >= 0 :
            pc_result += 45
        pc_result += 15
    return pc_result
def main() :
    """Post Office main"""
    envelop = int(input())
    package = int(input())

    en_result = 0
    pack_result = 0

    en_result = en(envelop)
    pack_result = pc(package)

    print(f"{en_result+pack_result:.0f}")
main()
