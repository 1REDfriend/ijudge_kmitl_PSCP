"""century"""
import math

def main():
    """century main"""
    num = int(input())
    text_list = []

    for _ in range(num):
        text = input()
        if text[:4] == "A.D.":
            text_list.append(math.ceil(int(text[5:])/100))
        elif text[:4] == "B.E.":
            century = int(text[5:]) - 543
            if century <= 0:
                text_list.append("ERROR")
            else:
                text_list.append(math.ceil(century/100))

    for i in text_list:
        print(i)
main()
