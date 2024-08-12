"""FOR!F-Ball"""
def find_ball_position(position,moves):
    """find_ball_position"""

    for move in moves:
        if move == 'A':
            if position == 1:
                position = 2
            elif position == 2:
                position = 1
        elif move == 'B':
            if position == 2:
                position = 3
            elif position == 3:
                position = 2
        elif move == 'C':
            if position == 1:
                position = 3
            elif position == 3:
                position = 1

    return position

def main() :
    """FOR!F-Ball main"""
    text = input().strip()
    position = 1
    for i in text :
        position = find_ball_position(position,i)
    print(position)
main()
