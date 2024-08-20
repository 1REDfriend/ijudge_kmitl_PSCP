"""FourDirections"""
def main():
    """FourDirections main"""
    text = input()

    up = [
        "  *  ",
        " *** ",
        "* * *",
        "  *  ",
        "  *  "
    ]
    down = [
        "  *  ",
        "  *  ",
        "* * *",
        " *** ",
        "  *  "
    ]
    left = [
        "  *  ",
        " *   ",
        "*****",
        " *   ",
        "  *  "
    ]
    right = [
        "  *  ",
        "   * ",
        "*****",
        "   * ",
        "  *  "
    ]

    figures = {'U': up, 'D': down, 'L': left, 'R': right}

    for i in range(5) :
        for x,o in enumerate(text) :
            print(figures[o][i] ,end=" ")
            if x >= len(text)-1 :
                print()
main()
