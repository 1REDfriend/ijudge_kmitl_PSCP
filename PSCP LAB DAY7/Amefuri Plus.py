"""Amefuri Plus"""
def main() :
    """Amefuri Plus"""
    start_h = int(input())
    weather = input().lower()
    hurican = False
    wet = 8
    for v in weather :
        if 6 <= start_h < 18 :
            if v == "c" :
                wet -= 0.5
            elif v == "n" :
                wet -= 1
            elif v == "w" :
                wet -= 1.5
        elif (0 <= start_h < 6) and (18 <= start_h<= 24) :
            if v == "c" :
                wet -= 0.25
            elif v == "n" :
                wet -= 0.5
            elif v == "w" :
                wet -= 0.75
        if v == "r" :
            wet += 2
        elif v == "s" :
            wet += 3
        elif v == "h" :
            hurican = True
            break
    if hurican :
        print("Lost")
    elif wet :
        print