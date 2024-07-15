"""Largest Number"""
def check_best_choice2(bs ,value , last) :
    """if true return value fix PEB-8"""
    if bs :
        return value
    return last
def check_best_choice(sl) :
    """check best choice"""
    s1,s2,s3,s4,s5,s6 = sl
    bs1 = s1>=s2 and s1>=s3 and s1>=s4 and s1>=s5 and s1>=s6
    bs2 = s2>=s1 and s2>=s3 and s2>=s4 and s2>=s5 and s2>=s6
    bs3 = s3>=s1 and s3>=s2 and s3>=s4 and s3>=s5 and s3>=s6
    bs4 = s4>=s1 and s4>=s2 and s4>=s3 and s4>=s5 and s4>=s6
    bs5 = s5>=s1 and s5>=s2 and s5>=s3 and s5>=s4 and s5>=s6

    best = -1
    best = check_best_choice2(bs1 , s1 , best)
    best = check_best_choice2(bs2 , s2 , best)
    best = check_best_choice2(bs3 , s3 , best)
    best = check_best_choice2(bs4 , s4 , best)
    best = check_best_choice2(bs5 , s5 , best)
    if not best == -1 :
        return best
    return s6
def find_best(allnum) :
    """sum all and find best choice"""

    sum1 = allnum[0] + allnum[1] + allnum[2]
    sum2 = allnum[0] + allnum[2] + allnum[1]

    sum3 = allnum[1] + allnum[2] + allnum[0]
    sum4 = allnum[1] + allnum[0] + allnum[2]

    sum5 = allnum[2] + allnum[0] + allnum[1]
    sum6 = allnum[2] + allnum[1] + allnum[0]

    best = check_best_choice([sum1,sum2,sum3,sum4,sum5,sum6])
    return best
def main() :
    """Largest Number"""
    num1 = input()
    num2 = input()
    num3 = input()

    allnum = [num1,num2,num3]
    best = find_best(allnum)
    print(best)
main()
