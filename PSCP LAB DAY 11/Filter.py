"""Filter"""
import json
def main() :
    """Filter main"""
    sc = json.loads(input())
    wait = float(input())

    sc = dict(filter(lambda x : x[1] >= wait,\
        sorted(sc.items(),key=lambda x : int(x[0]))))

    if sc:
        for i,j in sc.items() :
            print(i,f"{j:.2f}",sep="\t")
    else :
        print("Nope")

main()
