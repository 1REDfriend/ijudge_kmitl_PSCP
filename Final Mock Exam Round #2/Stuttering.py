"""Stuttering"""
def main():
    """Stuttering main"""
    txt_l = input().strip().split(" ")
    new_txt = []
    seen = set()

    for i in txt_l:
        if i not in seen:
            new_txt.append(i)
            seen.add(i)
        else :
            seen = set()

    print(" ".join(new_txt))

main()
