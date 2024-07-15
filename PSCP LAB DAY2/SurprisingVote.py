"""SurprisingVote"""
def main() :
    """SurprisingVote"""
    sumvote = float(input())
    maxvote = float(input())
    if maxvote*2 <= sumvote :
        vote3 = sumvote-(maxvote*2)
    else :
        vote3 = sumvote-maxvote
    if maxvote-2 <= vote3 <= maxvote :
        print("Not surprising")
    else :
        print("Surprising")
main()
