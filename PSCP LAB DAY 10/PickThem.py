"""PickThem"""
import json
def main() :
    """PickThem main"""
    has_been = False
    load = json.loads(input())
    for i in load :
        if not i % 2 :
            print(i)
            has_been = True
    if not has_been :
        print("Nope")
main()
