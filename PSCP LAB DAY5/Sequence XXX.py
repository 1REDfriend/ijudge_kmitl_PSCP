"""Sequence XXX"""
def main() :
    """Sequence XXX main"""
    boxWidth = int(input())
    boxCount = int(input())

    if boxWidth <= 1 :
        print("*"+(" "+"*")*(boxCount-1))
        return
    print("*"*(boxWidth) + (" "+("*"*boxWidth))*(boxCount-1))
    # boxWidth หาร 2 ไม่เอาเศษ แล้วลบออก 3 เพื่อเอาแค่ส่วนด้านบน
    for i in range((boxWidth-2)//2) :
        # ที่เอา (boxWidth-(i+i+4) คือ ขนาดของ space 2 ข้าง (i)
        # ขนาดของ * ที่มีอยู่
        print(f'*{(" "*i)}*{(" "*(boxWidth-(i+i+4)))}*{" "*i}*',end="")
        print((" "+(f'*{(" "*i)}*{(" "*(boxWidth-(i+i+4)))}*{" "*i}*'))*(boxCount-1))
    print(f'*{" "*((boxWidth//2)-1)}*{" "*((boxWidth//2)-1)}*' , end="")
    print((" "+(f'*{" "*((boxWidth//2)-1)}*{" "*((boxWidth//2)-1)}*'))*(boxCount-1))
    for i in range(((boxWidth-2)//2)-1,-1,-1) :
        print(f'*{(" "*i)}*{(" "*(boxWidth-(i+i+4)))}*{" "*i}*' , end="")
        print((" "+(f'*{(" "*i)}*{(" "*(boxWidth-(i+i+4)))}*{" "*i}*'))*(boxCount-1))
    print("*"*(boxWidth) + (" "+("*"*boxWidth))*(boxCount-1))
main()
