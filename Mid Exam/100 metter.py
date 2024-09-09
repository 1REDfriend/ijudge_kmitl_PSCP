"""100 meters"""
import math
def main() :
    """100 meters main"""
    n_win1 = 0
    n_win2 = 0
    n_win3 = 0

    win1_s = math.inf
    win2_s = math.inf
    win3_s = math.inf

    for i in range(1,9) :
        times = float(input())
        if win1_s > times :
            win3_s = win2_s
            win2_s = win1_s
            win1_s = times

            n_win3 = n_win2
            n_win2 = n_win1
            n_win1 = i
        elif win2_s > times :
            win3_s = win2_s
            win2_s = times

            n_win3 = n_win2
            n_win2 = i
        elif win3_s > times :
            win3_s = times

            n_win3 = i
    print(n_win1 ,n_win2 , n_win3)
main()
