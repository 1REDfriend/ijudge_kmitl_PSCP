n_m = map(int, input().split(" "))
red = list(map(int, input().split(" ")))
blue = list(map(int, input().split(" ")))

#ถ้าเลข n m ตัวครั้งแรกเป็นจุดตัด การนับ n m ครั้งต่อไปจะไม่นับ แต่ถ้านับ n ได้แล้วจะต้องลูป m ให้จนครบ <= n หลังจากนั้นค่อย
#เลื่อน n m นับต่อ

cross_counter = 1
is_same = True
is_same_count = 0

n_index = 0
m_index = 0

# 5 7
# 2 7 8 15 20
# 3 4 5 7 10 16 21

if len(blue) < len(red) :
    temp = red
    red = blue
    blue = temp

for n in red :
    if is_same and n_index == m_index:
        n_index += 1
        m_index += 1
        if is_same_count :
            is_same_count -= 1
            continue
        else :
            is_same = False
    else :
        check = False
        for i,m in enumerate(blue) :
            if i >= m_index :
                if m < n :
                    m_index += 1
                    cross_counter += 1
                    check = True
                elif m == n :
                    cross_counter += 1
                    is_same = True
                    check = True
                else :
                    if not check :
                        cross_counter += 1
                    break
        if not is_same :
            n_index += 1
        m_index += 1

print(cross_counter)