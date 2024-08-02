"""Align"""
def main():
    """Align"""
    size = int(input())
    alignment = input()
    text = input()
    if alignment == "left":
        print(f"{text:<{size}}")
    elif alignment == "center":
        space = " " * ((size - len(text)) // 2)
        space2 = " " * (((size - len(text))) % 2)
        print(f"{space + space2}{text}{space}")
    elif alignment == "right":
        print(f"{text:>{size}}")
main()
