"""Amefuri Plus"""


def time_push(time):
    """timer calculator"""
    time += 1
    if time > 23:
        time = 0
    return time


def day(wet, v):
    """day light"""
    if v == "c":
        wet -= 0.5
    elif v == "n":
        wet -= 1
    elif v == "w":
        wet -= 1.5
    return wet


def night(wet, v):
    """night light"""
    if v == "c":
        wet -= 0.25
    elif v == "n":
        wet -= 0.5
    elif v == "w":
        wet -= 0.75
    return wet


def main():
    """Amefuri Plus"""
    start_h = int(input())
    weather = input().lower()
    hurican = False
    wet = 8
    for v in weather:
        if 6 <= start_h < 18:
            wet = day(wet, v)
        elif (0 <= start_h < 6) or (18 <= start_h <= 24):
            wet = night(wet, v)

        if v == "r":
            wet += 2
        elif v == "s":
            wet += 3
        elif v == "h":
            hurican = True
            break
        if wet > 16:
            wet = 16
        elif wet <= 0:
            wet = 0
            break
        start_h = time_push(start_h)
    if hurican:
        print("Lost")
    elif wet:
        print(f'Still Wet (Wet Level: {wet:.2f})')
    else:
        print("Dry")


main()
