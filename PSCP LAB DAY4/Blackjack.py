"""Blackjack"""
def main() :
    """def"""
    number = int(input())
    score = 0
    stack_a = 0
    for _ in range(number) :
        card = input().upper().strip()
        if card in ("J" , "K" , "Q") :
            score += 10
        elif card.isnumeric() :
            card_value = int(card)
            if 2 <= card_value <= 10:
                score += card_value
        elif card == "A" :
            stack_a += 1
    for _ in range(stack_a) :
        if stack_a >= 2 :
            if score + 11 < 21 :
                score += 11
            else :
                score += 1
        else :
            if score + 11 <= 21 :
                score += 11
            else :
                score += 1
    print(score)
main()
