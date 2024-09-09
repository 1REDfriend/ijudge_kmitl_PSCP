"""Digital"""
def main() :
    """Digital main"""
    name = input()
    country = input()
    hasHomeCard = input()
    age = float(input())
    m_perYear = float(input())
    m_bank = float(input())

    result = True

    if age < 16 :
        result = False
    elif country in "No" or country in "False" :
        result = False
    elif hasHomeCard in "No" or country in "False" :
        result = False
    elif m_bank > 500_000 :
        result = False
    elif m_perYear > 840_000 :
        result = False
    if result :
        print(f'Congratulations! {name} ',end="")
        print('is qualified to receive a digital \
wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.',end="")
    else :
        print(f'Unfortunately, {name} is not qualified.')
main()
