"""CuteCat CuteFox"""

def find_len(category_dict, search_text):
    """len"""
    return len([value for value in category_dict.values() if search_text in value])

def main():
    """CuteCat CuteFox main"""
    entry_count, category_dict, result_dict = int(input()), {}, {}

    for _ in range(entry_count):
        input_text = str(input())

        if len(input_text.split('"')) > len(input_text.split("'")):
            category_dict[input_text.split('"')[1]] = input_text.split('"')[3]
        else:
            category_dict[input_text.split("'")[1]] = input_text.split("'")[3]
    cat_count, fox_count = find_len(category_dict, "Cat"), find_len(category_dict, "Fox")

    cat_present, fox_present, entry_flag = "Cat01" in category_dict.values(), \
        "Fox01" in category_dict.values(), 0

    if not cat_count  or not cat_present:
        result_dict["Garfield"] = "Cat01"
    if not fox_count or not fox_present:
        result_dict["Fubuki"] = "Fox01"

    for key, value in sorted(category_dict.items(), key=lambda x: x[1]):

        if not fox_present and value.count("Fox") >= 1 and not entry_flag:
            entry_flag += 1
            result_dict["Fubuki"] = "Fox01"
        result_dict[key] = value

    cat_count, fox_count = find_len(result_dict, "Cat"), \
        find_len(result_dict, "Fox")

    cat_entries, fox_entries = {}, {}

    for key, value in result_dict.items():
        if value.count("Cat") >= 1:
            cat_entries.update({int(value.split("Cat")[1]): [key, value]})
        elif value.count("Fox") >= 1:
            fox_entries.update({int(value.split("Fox")[1]): [key, value]})

    print(f"Cat : {cat_count}\nFox : {fox_count}")

    for cat_key in sorted(cat_entries):
        print(cat_entries[cat_key][0] + " : " + cat_entries[cat_key][1])
    for fox_key in sorted(fox_entries):
        print(fox_entries[fox_key][0] + " : " + fox_entries[fox_key][1])

main()
