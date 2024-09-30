"""Palindrome"""
def main() :
    """Palindrome main"""

    num = int(input())
    now_time = input()

    now_time = now_time[:now_time.find(":")] + now_time[now_time.find(":") + 1:]
    counter = 0

    while counter < num :
        now_time = str(int(now_time) + 1)

        if int(now_time[-2:]) > 59 :
            now_time = str((int(now_time) - 60) + 100)

        if int(now_time) > 2359 :
            now_time = "0" + str(int(now_time) - 2400)

        if len(now_time) < 3 :
            now_time = f"{now_time:>03}"
        now_time_b = now_time[::-1]

        if now_time == now_time_b :
            counter += 1
            print(f"{now_time[:-2]:>01}:{now_time[-2:]:>02}")
main()
