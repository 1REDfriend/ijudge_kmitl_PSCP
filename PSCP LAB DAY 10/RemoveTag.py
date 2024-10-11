"""RemoveTag"""
def main() :
    """RemoveTag"""
    html = input().replace("/","")
    tag_count = html.count("<")
    for i in range(tag_count) :
        