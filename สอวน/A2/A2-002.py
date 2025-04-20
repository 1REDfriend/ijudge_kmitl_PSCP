pole = int(input())
pole_list = []
max_tent = 0

min_pole_x = 0
max_pole_x = 0
min_pole_y= 0
max_pole_y = 0

for _ in range(pole) :
    x,y = map(int, input().split(" "))
    pole_list.append([x,y])
    min_pole_x = min(x, min_pole_x)
    min_pole_y = min(y , min_pole_y)
    max_pole_x = max(x, max_pole_x)
    max_pole_y = max(y, max_pole_y)

# [[1,2],[5,6],[4,3],[7,4],[6,1],[8,0]]

for i1,pole_pos in enumerate(pole_list) :
    x,y = map(int, pole_pos)
    for i2,check_pos in enumerate(pole_list) :
        if i1 == i2 :
            continue
        # หาแบบสี่เหลี่ยมจัตุรัส
        if abs(x-check_pos[0]) == abs(y-check_pos[1]):
            max_tent = max(max_tent, abs(x-check_pos[0]))

print(max_tent)