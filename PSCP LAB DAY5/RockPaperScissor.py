"""RockPaperScissor"""
def main() :
    """RockPaperScissor"""
    text = input()
    user1 = 0
    user2 = 0
    for i in range(len(text)//2) :
        temp = text[i*2:(i*2)+2]
        if temp[0] == "S" and temp[1] == "R" :
            user2 += 1
        if temp[0] == "S" and temp[1] == "P" :
            user1 += 1
        if temp[0] == "R" and temp[1] == "P" :
            user2 += 1
        
        if temp[1] == "S" and temp[0] == "R" :
            user1 += 1
        if temp[1] == "S" and temp[0] == "P" :
            user2 += 1
        if temp[1] == "R" and temp[0] == "P" :
            user1 += 1
main()
