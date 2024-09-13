"""Duplicate I"""
def main() :
    """Duplicate I main"""
    m = int(input())
    n = int(input())
    m_dt = {}
    n_dt = {}
    result = False
    for _ in range(m) :
        student_id = input()
        if m_dt.get(student_id) is None :
            m_dt.update({student_id : 0})
    for _ in range(n) :
        student_id = input()
        if n_dt.get(student_id) is None :
            n_dt.update({student_id : 0})
    for i in sorted(m_dt ,reverse=True) :
        if i in sorted(n_dt) :
            print(i)
            result = True
            continue
    if not result :
        print("Nope")
main()
