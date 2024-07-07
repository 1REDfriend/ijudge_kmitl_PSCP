"""Pre - Kayak"""
def main() :
    """Pre - Kayak"""
    int(input().strip())
    party = input().strip().split(" ")
    party = sorted(list(map(int, party)))

    sums = 0

    for v in party :
        if party.count(v) >= 2 :
            for _ in range(party.count(v)//2) :
                party.remove(v)
                party.remove(v)
    party = sorted(party)

    party_temp = []

    while len(party) > 2 :
        maxs = max(party)
        for i in range(len(party) - 1) :
            diff = abs(party[i+1] - party[i])
            if diff < maxs :
                maxs = diff
                party_temp = [party[i] , party[i+1]]
        sums += maxs
        party.remove(party_temp[0])
        party.remove(party_temp[1])
    print(sums)
main()
