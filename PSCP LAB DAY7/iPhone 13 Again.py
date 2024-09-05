"""iPhone 13 Again"""


def mini(storage):
    """mini"""
    if storage == "128 GB":
        print(25_900)
    elif storage == "256 GB":
        print(29_900)
    elif storage == "512 GB":
        print(37_900)
    else:
        print("Not Available")


def normal(storage):
    """13"""
    if storage == "128 GB":
        print(29_900)
    elif storage == "256 GB":
        print(33_900)
    elif storage == "512 GB":
        print(41_900)
    else:
        print("Not Available")


def pro(storage):
    """pro"""
    if storage == "128 GB":
        print(38_900)
    elif storage == "256 GB":
        print(42_900)
    elif storage == "512 GB":
        print(50_900)
    elif storage == "1 TB":
        print(58_900)
    else:
        print("Not Available")


def promax(storage):
    """pro max"""
    if storage == "128 GB":
        print(42_900)
    elif storage == "256 GB":
        print(46_900)
    elif storage == "512 GB":
        print(54_900)
    elif storage == "1 TB":
        print(62_900)
    else:
        print("Not Available")


def main():
    """iPhone 13 Again main"""
    brand = input().strip()
    storage = input().strip()

    if brand == "iPhone 13 mini":
        mini(storage)
    elif brand == "iPhone 13":
        normal(storage)
    elif brand == "iPhone 13 Pro":
        pro(storage)
    elif brand == "iPhone 13 Pro Max":
        promax(storage)
    else :
        print("Not Available")


main()
