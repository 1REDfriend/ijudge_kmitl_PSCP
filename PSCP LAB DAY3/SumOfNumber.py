'''ddd'''
def main():
    '''main'''
    vaule = 0
    need = int(input())
    while need >= 0:
        num = int(input())
        if num == -1 or vaule + num == need:
            if num != -1 :
                vaule += num
            break
        vaule += num
    print(vaule)
main()
