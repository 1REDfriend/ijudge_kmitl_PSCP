"""Grade III"""
def check_grade(score) :
    """ได้เตรียมตัวอ่านหนังสือ"""
    grade = 0
    if score >= 95 :
        grade = 4
    elif score >= 90 :
        grade = 3.5
    elif score >= 85 :
        grade = 3
    elif score >= 80 :
        grade = 2.5
    elif score >= 75 :
        grade = 2
    elif score >= 70 :
        grade = 1.5
    elif score >= 65 :
        grade = 1
    elif score >= 60 :
        grade = 0.5
    else:
        grade = 0
    return grade

def main() :
    """Grade III"""
    number = int(input())
    last = 0
    for _ in range(number) :
        grade = float(input())
        grade = check_grade(grade)
        last += grade
    last = str(last/number)
    grader = ""

    timer = False
    count = 3
    for i in last :
        if count > 0 :
            grader += i
            if i == "." :
                timer = True
            if timer :
                count -= 1
        else :
            break
    print(f"{float(grader):.2f}")
main()
