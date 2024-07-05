"""Gift II"""
def main():
    """Gift II"""
    sums = 0
    for _ in range(8):
        gift = int(input())
        if not gift % 2 :
            sums += gift
    print(sums)
main()
