"""Timing II"""
def main() :
    """Timing II"""
    times = int(input())
    days = times // 86400
    times = times % 86400
    hour = times // 3600
    times %= 3600
    minutes = times // 60
    seconds = times % 60
    if days > 9999 :
        print("ERR_:__:__:__")
        return
    print(f"{days:04d}:{hour:02d}:{minutes:02d}:{seconds:02d}")
main()
