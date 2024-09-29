"""Volleyball"""
def check(text_score, r) :
    """check a vally balllllll"""
    team_a = 0
    team_b = 0
    err = 0
    c = ""
    w = "c"
    for i in text_score :
        if not err :
            if i == "A" :
                team_a += 1
            else :
                team_b += 1
            if r < 5 :
                if team_a >= 25 and team_a - team_b >= 2 :
                    w = "a"
                    err += 1
                elif team_b >= 25 and team_b - team_a >= 2 :
                    w = "b"
                    err += 1
            else :
                if team_a >= 15 and team_a - team_b >= 2 :
                    w = "a"
                    err += 1
                elif team_b >= 15 and team_b - team_a >= 2 :
                    w = "b"
                    err += 1
            c += ""
        else :
            c += i
    return c, w, f"Set {r}: A ({team_a}) | B ({team_b})"

def main() :
    """Volleyball main"""
    text_score = input()

    team_a = 0
    team_b = 0
    jack = 0

    for i in range(1,6) :
        len_s = len(text_score)
        if not len_s or team_a == 3 or team_b == 3 :
            break
        text_score, w, re = check(text_score, i)
        print(re)
        if w == "a" :
            team_a += 1
        elif w == "b" :
            team_b += 1
        jack = i

    if jack == 5 or team_a == 3 or team_b == 3 :
        if team_a > team_b :
            print(f"A won {team_a}:{team_b} set")
        elif team_a < team_b :
            print(f"B won {team_b}:{team_a} set")
        else :
            print("The game has not finished yet.")
    else :
        if team_a + team_b == jack :
            print(f"Set {i}: A (0) | B (0)")
        print("The game has not finished yet.")

main()
