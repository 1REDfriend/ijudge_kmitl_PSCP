"""MissingCard No Set"""
def main() :
    """MissingCard No Set main"""
    rank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    word = ["S","H","D","C"]
    total_card = []

    for i in word :
        for n in rank :
            total_card.append(f"{n}{i}")

    for _ in range(51) :
        total_card.remove(input())

    print("".join(total_card))

main()
