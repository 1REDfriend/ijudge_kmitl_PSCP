"""Safe"""
def main() :
    """Safe main"""
    word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    code_txt1 = input()
    code_txt2 = input()

    count = 0
    time = 0

    while count < len(code_txt1) :

        time += min(abs(word.find(code_txt1[count]) - word.find(code_txt2[count])),\
            abs(word.find(code_txt1[count]) - word.find(code_txt2[count]) - 26),
            abs(word.find(code_txt1[count]) - word.find(code_txt2[count]) + 26))

        count += 1
    print(time)

main()
