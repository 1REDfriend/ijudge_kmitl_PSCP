"""KFC"""
def is_hex(s):
    """base 16 detect"""
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def main():
    """MAC main"""
    mac = input()

    if mac.count("-") == 5 and all(len(part) == 2 \
and is_hex(part) for part in mac.split("-")):
        print("VALID 1")
    elif mac.count(":") == 5 and all(len(part) == 2 \
and is_hex(part) for part in mac.split(":")):
        print("VALID 2")
    elif mac.count(".") == 2 and all(len(part) == 4 \
and is_hex(part) for part in mac.split(".")):
        print("VALID 3")
    else:
        print("ERROR")

main()
