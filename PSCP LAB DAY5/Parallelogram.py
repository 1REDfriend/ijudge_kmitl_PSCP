"""Parallelogram"""
def main() :
    """Parallelogram main"""
    text = input()
    for i,_ in enumerate(text) :
        countText= len(text)
        print(f"{text[:i+1]:>{countText}}")
    for i,_ in enumerate(text) :
        if i+2 > len(text) :
            break
        print(f"{text[i+1:]}")
main()
