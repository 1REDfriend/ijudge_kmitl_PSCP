"""Run Length Encoding"""
def main() :
    """Run Length Encodind main"""
    text = input()
    lastWord = ''
    stackTemp = ''
    result = ''
    for i,v in enumerate(text) :
        if lastWord != v :
            couter = 0
            if i > 0 :
                for _ in stackTemp :
                    couter += 1
                result += str(couter)+lastWord
                stackTemp = ''
            lastWord = v
        stackTemp += v

    if stackTemp :
        couter = 0
        for _ in stackTemp :
            couter += 1
        result += str(couter)+lastWord
        stackTemp = ''
    print(result)
main()
