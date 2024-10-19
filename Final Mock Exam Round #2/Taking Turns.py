"""Taking Turns"""
import json
def main() :
    """Taking Turns main"""
    txt = input().strip()
    n_list = json.loads(txt) if txt else txt
    i = -1
    result = []
    while n_list :
        result.append(n_list[i])
        n_list.pop(i)
        i = 0 if i == -1 else -1
    print(result)
main()