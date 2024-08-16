"""Turnstile"""
def main():
    """Turnstile MAIN"""
    doorState = 'Close'
    result = 0
    while True:
        text = input()
        if text == "END":
            break
        if text == "C" :
            doorState = 'Open'
        elif text == "P" :
            if doorState == 'Open' :
                result = result + 1
                doorState = 'Close'
    print(result)
main()
