"""BrickBridge"""
def main() :
    """Main"""
    normal_brick = int(input())
    big_brick = int(input())
    goal = int(input())

    use_big = goal//5
    if use_big > big_brick :
        use_big = big_brick
        goal -= use_big*5

        normal_brick2 = goal-normal_brick
    else :
        goal -= use_big*5

        normal_brick2 = goal-normal_brick

    if normal_brick2 > 0:
        print(-1)
    else :
        print(normal_brick+normal_brick2)
main()
