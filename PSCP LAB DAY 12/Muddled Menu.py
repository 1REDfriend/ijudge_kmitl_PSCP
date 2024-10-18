"""Muddled Menu"""


def main():
    """Muddled Menu main"""
    menu_list = []

    while True:
        menu = input()
        if menu == "CLOSED":
            print("Full Course: [] Reversed: []")
            return

        if menu != "DONE":
            if menu == "SOMETHING'S WRONG":
                menu_list.clear()
                continue
            if menu[:10] == "Can't do: ":
                menu_list.remove(menu[10:])
            else:
                text = menu.split(" #")
                if text[1].isnumeric():
                    menu_list.insert(int(text[1]) - 1, text[0])
                else:
                    menu_list.append(text[0])
        else:
            break

    print(f"Full Course: {menu_list}", end=" ")
    menu_list.reverse()
    print(f"Reversed: {menu_list}")

if __name__ == "__main__":
    main()
