
# Project Euler problem 54: poker hands

file_path = "p54.txt"
with open(file_path, 'r') as f:
    poker_data = f.read()

card_values = {rank: i for i, rank in enumerate('23456789TJQKA', 2)}

def get_hand_rank(hand): # Separates card ranks and suits, and sort ranks
    ranks = sorted([card_values[c[0]] for c in hand])
    suits = [c[1] for c in hand]

    is_flush = len(set(suits)) == 1

    is_straight = ranks == list(range(ranks[0], ranks[0] + 5)) # Checks for a straight

    is_low_straight = sorted(ranks) == [2, 3, 4, 5, 14]

    counts = {}
    for r in ranks:
        counts[r] = counts.get(r, 0) + 1

    # Royal Flush / Straight Flush
    if (is_straight or is_low_straight) and is_flush:
        if ranks[-1] == 14:
            return (9, [14, 13, 12, 11, 10])
        if is_low_straight:
            return (8, [5, 4, 3, 2, 1])
        return (8, ranks)

    fours = [r for r, count in counts.items() if count == 4]
    if fours:
        return (7, fours[0], [r for r in ranks if r != fours[0]])

    threes = [r for r, count in counts.items() if count == 3]
    pairs = [r for r, count in counts.items() if count == 2]
    if threes and pairs:
        return (6, threes[0], pairs[0])

    if is_flush:
        return (5, sorted(ranks, reverse=True))

    if is_straight or is_low_straight:
        if is_low_straight:
            return (4, [5, 4, 3, 2, 1])
        return (4, ranks)

    if threes:
        return (3, threes[0], sorted([r for r in ranks if r != threes[0]], reverse=True))

    if len(pairs) == 2:
        return (2, sorted(pairs, reverse=True), sorted([r for r in ranks if r not in pairs], reverse=True))

    if len(pairs) == 1:
        return (1, pairs[0], sorted([r for r in ranks if r != pairs[0]], reverse=True))

    return (0, sorted(ranks, reverse=True))

def solve():
    player_1_wins = 0
    hands = poker_data.strip().split('\n')

    for line in hands:
        cards = line.split(' ')
        player1_hand = cards[:5]
        player2_hand = cards[5:]

        player1_rank = get_hand_rank(player1_hand)
        player2_rank = get_hand_rank(player2_hand)

        if player1_rank > player2_rank:
            player_1_wins += 1

    return player_1_wins

if __name__ == "__main__":
    result = solve()
    print(result)