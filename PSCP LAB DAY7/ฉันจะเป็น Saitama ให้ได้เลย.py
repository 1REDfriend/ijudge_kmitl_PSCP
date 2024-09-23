"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math


def main():
    """ฉันจะเป็น Saitama ให้ได้เลย main"""
    ground = int(input())
    situp = int(input())
    updown = int(input())
    run = int(input())

    oneD_ground = int(input())
    oneD_situp = int(input())
    oneD_run = int(input())
    oneD_updown = int(input())

    ground = math.ceil(ground / oneD_ground)
    situp = math.ceil(situp / oneD_situp)
    updown = math.ceil(updown / oneD_updown)
    run = math.ceil(run / oneD_run)

    result = ground
    if situp > result:
        result = situp
    if updown > result:
        result = updown
    if run > result:
        result = run

    print(result)


main()
