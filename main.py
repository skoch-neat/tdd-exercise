VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    INVALID_MSG = "Invalid"
    BUST_MSG = "BUST"

    score = 0
    num_aces = hand.count('Ace')

    for card in hand:
        if card not in VALID_CARDS:
            return INVALID_MSG
        if len(hand) > 5:
            return INVALID_MSG
        if isinstance(card, str) and card == ACE_CARD:
            card = 11
        elif isinstance(card, str):
            card = 10
        # if card in hand:
        score += card

    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1

    if score > 21:
        return BUST_MSG
    
    return score