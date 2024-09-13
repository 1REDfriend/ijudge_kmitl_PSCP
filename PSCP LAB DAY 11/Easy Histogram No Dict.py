"""Easy Histogram No Dict"""
def main() :
    """Easy Histogram No Dict main """
    text = input()
    text_list = []
    last_text = ''
    counter = 1
    for i in text :
        text_list.append(i)
    text_list = sorted(text_list , key=lambda x : (x.islower() ,x.isupper()))
    print(text_list)
    for i in text_list :
        if not last_text :
            last_text = i
        else :
            if last_text == i :
                counter = counter + 1
            else :
                print(f'{last_text} = {counter}')
                last_text = ''
                counter = 1
main()
