"""Meteorite"""
def main() :
    """Meteorite main"""
    meteoriteKG = float(input())
    exploteM = int(input())
    safeKG = float(input())

    airStrike = 0
    count = 1
    if meteoriteKG >= safeKG :
        airStrike += 1
        meteoriteKG /= exploteM
    while meteoriteKG >= safeKG :
        airStrike += exploteM**count
        meteoriteKG /= exploteM
        count += 1
    print(airStrike)
main()
