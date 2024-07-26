"""fjseifjise"""

def main():
    """main"""
    item_arr = []
    best_price = 0
    max_valocity = 0
    best_price_v2 = 0
    count_items = int(input())
    for _ in range(count_items):
        item_arr_temp = [float(input()),float(input())]
        item_arr.append(item_arr_temp)
    for i,v in enumerate(item_arr) :
        if v[1]/v[0] > max_valocity :
            max_valocity = v[1]/v[0]
            best_price = i
            best_price_v2 = v[0]
        elif v[1]/v[0] == max_valocity :
            if v[0] < best_price_v2 :
                max_valocity = v[1]/v[0]
                best_price = i
    print(f"{item_arr[best_price][0]:.2f} {item_arr[best_price][1]:.2f}")
main()
