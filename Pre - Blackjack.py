"""Blackjack"""
def main() :
    """def"""
    number = int(input())
    score = 0
    for i in range(number) :
        card = input()
        if i > 1 :
            if score >= 17 :
                if card in ("J" , "K" , "Q") :
                    score += 10
                elif card == "A" :
                    if score <= 10 :
                        score += 11
                    else :
                        score += 1
                else:
                    card_value = int(card)
                    if 2 <= card_value <= 10:
                        score += card_value
        else :
            if card in ("J" , "K" , "Q") :
                    score += 10
            elif card == "A" :
                if score <= 10 :
                    score += 11
                else :
                    score += 1
            else:
                card_value = int(card)
                if 2 <= card_value <= 10:
                    score += card_value
    print(score)
main()
