"""Pre - Kayak"""
def main() :
    """def"""
    num = int(input())
    member_weight = input().split(" ")
    party_member = 2*num
    kayak_double = num-1
    kayak_normal = 2
    sums = 0

    member_weight = [int(i) for i in member_weight]
    member_weight = sorted(member_weight)
    member_weight.pop()
    member_weight.pop()
    print(member_weight)

    for i in range(len(member_weight) // 2) :
        i *= 2
        sums += abs(int(member_weight[i]) - int(member_weight[i + 1]))
    
    print(sums)
main()
