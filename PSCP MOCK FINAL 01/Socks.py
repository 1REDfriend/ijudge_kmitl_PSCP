"""Socks"""
def main() :
    """Socks main"""
    socks = [x for x in input()]
    socks.sort()

    new_sock = []
    for _ in range(len(socks)) :
        if len(socks) > 1 :
            if socks[0] == socks[1] :
                new_sock.append(socks[1]*2)
                socks.pop(0)
                socks.pop(0)
            else :
                socks.pop(0)
    if not len(new_sock) :
        print("None")
    else :
        print(" ".join(new_sock))
    print(len(new_sock))
main()
