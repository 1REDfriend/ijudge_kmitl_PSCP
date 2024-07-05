"""SaveComputeRepeat"""
def main():
    """SaveComputeRepeat"""
    start = 492137954293754252786
    millisec = start
    sec = millisec//1000
    millisec = millisec%1000
    minutes = sec//60
    sec = sec%60
    hour = minutes//60
    minutes = minutes%60
    days = hour//24
    hour = hour%24
    print(days,hour,minutes,sec,millisec)
main()
