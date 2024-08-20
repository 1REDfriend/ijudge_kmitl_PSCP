"""Ping"""
def main() :
    """Ping main"""
    command = input()
    input()
    pingingData = input()

    domain = command[command.find("ping")+5:]
    ip = ''

    if domain[:2].isnumeric() :
        ip = domain
    else :
        ip = pingingData[pingingData.find("[")+1:pingingData.find("]")]

    receiv = 0
    lost = 0
    minTime = float('inf')
    maxTime = 0
    allTime = 0

    for _ in range(4) :
        reply = input()
        if reply.find("Reply") > -1 :
            receiv += 1

            time = reply[reply.find("time")+5:reply.find("ms")]
            timeChoice = reply[reply.find("time")+4:reply.find("time")+5]
            if timeChoice == "<" :
                minTime = 0
            else :
                minTime = min(minTime , int(time))
                maxTime = max(maxTime , int(time))
                allTime += int(time)
        else :
            lost += 1

    print(f"Ping statistics for {ip}:")
    if lost >= 4 :
        print('    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),')
    else :
        print(f'    Packets: Sent = 4, Received = {receiv}, Lost = {lost} \
({(lost/4)*100:.0f}% loss),')
        print('Approximate round trip times in milli-seconds:')
        print(f'    Minimum = {minTime}ms, Maximum = {maxTime}ms, Average = {allTime//receiv}ms')
main()
