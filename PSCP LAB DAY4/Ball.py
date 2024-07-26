"""ksefekso"""
def ball():
    """okewijrfioweoj"""
    time = -1
    ball_hight = float(input())
    while ball_hight >= 0.01:
        ball_hight = ball_hight *(3/5)
        # print(f"{ball_hight:.2f}")
        time += 1
    print(time)

ball()
