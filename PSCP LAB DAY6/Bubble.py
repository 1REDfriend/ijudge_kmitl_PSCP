"""Bubble"""
def main() :
    """Bubble main"""
    text = input()
    lastBubble = ''
    jumpCount = 1
    canJump = 1
    result = ''
    for i in text :
        if canJump > 0 and i != "^" and i != "|":
            canJump -= 1
            if lastBubble == "O" :
                canJump -= 1
                lastBubble = i
                continue
            elif i == " " and lastBubble == "o":
                result = "IMPOSSIBLE"
                jumpCount = 1
                canJump = 0
            if i == "o" :
                jumpCount += 1
                lastBubble = i
                canJump = 1
            elif i == "O" :
                jumpCount += 1
                lastBubble = i
                canJump = 2
            elif i == " " :
                if lastBubble == "o" :
                    result = 'IMPOSSIBLE'
                    canJump = 0
                    jumpCount = 1
        if canJump <= 0 and i != "^" and i != "|":
            jumpCount += 1
    print(result)
    print(jumpCount)
main()
