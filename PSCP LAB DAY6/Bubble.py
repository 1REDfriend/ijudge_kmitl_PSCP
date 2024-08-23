"""Bubble"""
def main() :
    """Bubble main"""
    text = input()
    jumping = 0
    bigjump = False
    lastBubble = ''
    result = 'POSSIBLE'
    for i in text :
        if bigjump :
            jumping += 1
            lastBubble = i
            bigjump = False
            continue
        if i != "^" and i != "|" and result == 'POSSIBLE':
            if i == "o" :
                jumping += 1
            elif i == "O" :
                jumping += 1
                bigjump = True
            elif i == " " :
                if lastBubble == "O" :
                    jumping += 1
                    continue
                elif lastBubble == "o" :
                    jumping = 1
                    result = "IMPOSSIBLE"
                    continue
        elif result == 'IMPOSSIBLE' :
            jumping += 1
    print(result)
    print(jumping)
main()
