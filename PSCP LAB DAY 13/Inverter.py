'''Inverter'''
def main():
    '''Smth'''
    x = str(input())
    op = ''
    for char in x:
        if char == '0':
            op += '1'
        elif char == '1':
            op += '0'
    op = int(op)
    if not op :
        op = ''
    print(op)

main()
