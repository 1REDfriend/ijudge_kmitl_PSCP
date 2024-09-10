"""Game"""
def main() :
    """Game main"""
    scoreA = int(input())
    scoreB = int(input())

    scoreA = scoreA % 3
    scoreB = scoreB % 3

    if scoreB == scoreA :
        print(scoreA)
    else :
        print("Error")
main()
