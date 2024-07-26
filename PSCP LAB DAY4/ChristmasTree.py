"""ChristmasTree"""
def main() :
    """main"""
    leaf = int(input())
    logs = int(input())
    for i in range(leaf) :
        print(f"{' '*(leaf-i-1)}{'*'*i}*{'*'*i}")
    for i in range(logs) :
        print(f"{' '*(leaf-2)}---")
main()
