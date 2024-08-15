"""Sequence XXX"""
def main() :
    """Sequence XXX main"""
    boxWidth = int(input())
    boxCount = int(input())

    print("*"*(boxWidth) + (" "+("*"*boxWidth))*(boxCount-1))
    # boxWidth หาร 2 ไม่เอาเศษ แล้วลบออก 3 เพื่อเอาแค่ส่วนด้านบน
    for i in range((boxWidth-2)//2) :
        print(f'*{(" "*i)}*{(" "*(((boxWidth)//2)))}*{" "*i}*')
    print("*"*(boxWidth) + (" "+("*"*boxWidth))*(boxCount-1))
main()
