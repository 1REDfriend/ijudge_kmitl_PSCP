"""Bubble"""
def main() :
    """Bubble main"""
    text = input()
    jumping = 1
    canJump = True
    skip = 0
    result = 'POSSIBLE'

    for i,v in enumerate(text) :
        if not canJump :
            jumping += 1
            continue
        if skip > 0 :
            skip -= 1
            continue
        if v == "o" :
            jumping += 1
        elif v == "O" :
            jumping += 1
            if "|" in text[i+1:i+4] :
                skip = 3
            elif text[i+2:i+3] == " " or text[i+2:i+3] == "o" :
                skip = 2
            elif text[i+1:i+2] == " " or text[i+1:i+2] == "o":
                skip = 1

        elif v == " " :
            result = "IMPOSSIBLE"
            jumping = 1
            canJump = False
    print(result)
    print(jumping)
main()
