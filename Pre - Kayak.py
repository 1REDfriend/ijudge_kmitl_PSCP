"""Pre - Kayak"""
def main() :
    """def"""
    num = int(input())
    member_weight = input().split(" ")
    sums = 0

    member_weight = [int(i) for i in member_weight]
    member_weight = sorted(member_weight)
    print(member_weight)
    member_weight.pop(len(member_weight)-1)
    member_weight.pop(len(member_weight)-1)
    print(member_weight)
    for i in range(num-1) :
        i *= 2
        sums += abs(int(member_weight[i + 1] - int(member_weight[i])))

    print(sums)
main()
