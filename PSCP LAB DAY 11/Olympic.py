"""Olympic"""
def main() :
    """Olympic main"""
    num = int(input())

    player = {}
    current_sc = []

    place = 0
    current_p = 0

    country = None
    medals = None

    for _ in range(num) :

        txt = input()
        country = txt.split()[0]
        medals = list(map(int, txt.split()[1:]))
        player.update({country : medals})

    player = sorted(player.items(),key=lambda x : x[1],reverse=True)

    for i, _ in enumerate(player) :
        for v in range(i) :
            if player[v][1] == player[i][1] and player[v][0] > player[i][0]:
                player[v],player[i] = player[i],player[v]
    player = dict(player)

    for i,v in player.items() :
        current_p += 1
        if v != current_sc :
            current_sc = v
            place = current_p
            print(current_p,end=" ")
        else :
            print(place,end=" ")

        print(i," ".join(map(str,v)),sum(v))

main()
