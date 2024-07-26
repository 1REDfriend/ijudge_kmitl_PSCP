"""ksjefilfsilfe"""

def main():
    """ekafesjf"""
    sec_mutiverse = int(input())
    sec_to_min = int(input())
    min_to_hour = int(input())
    hour_to_day = int(input())

    sec_mutiverse %= sec_to_min * min_to_hour * hour_to_day
    hour = sec_mutiverse // (sec_to_min * min_to_hour)
    sec_mutiverse %= sec_to_min * min_to_hour
    minute = sec_mutiverse // sec_to_min
    sec_mutiverse %= sec_to_min
    second = sec_mutiverse

    print(f"{hour}:{minute}:{second}")

main()
