"""Bubble"""
def main() :
    """Bubble main"""
    text = input().strip()
    jump = 1
    con = 0
    result = "POSSIBLE"
    for i,v in enumerate(text) :
        if con :
            con -= 1
            continue
        if result == "POSSIBLE" :
            if v == "o" :
                jump += 1
            elif v == "O" :
                jump += 1
                st_text = text[i+1:i+4]
                if st_text.find("|") != -1:
                    con = st_text.find("|")
                elif st_text.find("O") != -1 :
                    con = 2 - st_text[::-1].find("O")
                elif st_text[::-1].find("o") != -1 :
                    con = 2 - st_text[::-1].find("o")
            elif v == " " :
                result = "IMPOSSIBLE"
                jump = 1
        else :
            jump += 1
    print(result)
    print(jump)
main()
