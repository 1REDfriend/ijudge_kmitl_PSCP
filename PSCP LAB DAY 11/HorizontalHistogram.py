"HorizontalHistogram"
def lower(value) :
    "lower before upper"

    value = value[0]
    if value.islower() :
        return 1,value
    return 2,value

def main() :
    "HorizontalHistogram main"
    hg = {}
    txt = str(input())
    for i in txt :
        hg.setdefault(i,"")
        if not len(hg[i].replace("|","")) % 5 and hg[i] :
            hg[i] += "|"
        hg[i] += "-"

    hg = dict(sorted(hg.items(),key=lower))
    for i, v in hg.items() :
        print(i,":",v)

main()
