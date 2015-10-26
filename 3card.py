#!/usr/bin/env python

from __future__ import division
from random import randint
print('Welcome to 3 Card Poker.')

deck = {
    0: {'name': 'AS', 'suit': 'Spades', 'val': 14},
    1: {'name': '2S', 'suit': 'Spades', 'val': 2},
    2: {'name': '3S', 'suit': 'Spades', 'val': 3},
    3: {'name': '4S', 'suit': 'Spades', 'val': 4},
    4: {'name': '5S', 'suit': 'Spades', 'val': 5},
    5: {'name': '6S', 'suit': 'Spades', 'val': 6},
    6: {'name': '7S', 'suit': 'Spades', 'val': 7},
    7: {'name': '8S', 'suit': 'Spades', 'val': 8},
    8: {'name': '9S', 'suit': 'Spades', 'val': 9},
    9: {'name': '10S', 'suit': 'Spades', 'val': 10},
    10: {'name': 'JS', 'suit': 'Spades', 'val': 11},
    11: {'name': 'QS', 'suit': 'Spades', 'val': 12},
    12: {'name': 'KS', 'suit': 'Spades', 'val': 13},
    13: {'name': 'AH', 'suit': 'Hearts', 'val': 14},
    14: {'name': '2H', 'suit': 'Hearts', 'val': 2},
    15: {'name': '3H', 'suit': 'Hearts', 'val': 3},
    16: {'name': '4H', 'suit': 'Hearts', 'val': 4},
    17: {'name': '5H', 'suit': 'Hearts', 'val': 5},
    18: {'name': '6H', 'suit': 'Hearts', 'val': 6},
    19: {'name': '7H', 'suit': 'Hearts', 'val': 7},
    20: {'name': '8H', 'suit': 'Hearts', 'val': 8},
    21: {'name': '9H', 'suit': 'Hearts', 'val': 9},
    22: {'name': '10H', 'suit': 'Hearts', 'val': 10},
    23: {'name': 'JH', 'suit': 'Hearts', 'val': 11},
    24: {'name': 'QH', 'suit': 'Hearts', 'val': 12},
    25: {'name': 'KH', 'suit': 'Hearts', 'val': 13},
    26: {'name': 'AC', 'suit': 'Clubs', 'val': 14},
    27: {'name': '2C', 'suit': 'Clubs', 'val': 2},
    28: {'name': '3C', 'suit': 'Clubs', 'val': 3},
    29: {'name': '4C', 'suit': 'Clubs', 'val': 4},
    30: {'name': '5C', 'suit': 'Clubs', 'val': 5},
    31: {'name': '6C', 'suit': 'Clubs', 'val': 6},
    32: {'name': '7C', 'suit': 'Clubs', 'val': 7},
    33: {'name': '8C', 'suit': 'Clubs', 'val': 8},
    34: {'name': '9C', 'suit': 'Clubs', 'val': 9},
    35: {'name': '10C', 'suit': 'Clubs', 'val': 10},
    36: {'name': 'JC', 'suit': 'Clubs', 'val': 11},
    37: {'name': 'QC', 'suit': 'Clubs', 'val': 12},
    38: {'name': 'KC', 'suit': 'Clubs', 'val': 13},
    39: {'name': 'AD', 'suit': 'Diamonds', 'val': 14},
    40: {'name': '2D', 'suit': 'Diamonds', 'val': 2},
    41: {'name': '3D', 'suit': 'Diamonds', 'val': 3},
    42: {'name': '4D', 'suit': 'Diamonds', 'val': 4},
    43: {'name': '5D', 'suit': 'Diamonds', 'val': 5},
    44: {'name': '6D', 'suit': 'Diamonds', 'val': 6},
    45: {'name': '7D', 'suit': 'Diamonds', 'val': 7},
    46: {'name': '8D', 'suit': 'Diamonds', 'val': 8},
    47: {'name': '9D', 'suit': 'Diamonds', 'val': 9},
    48: {'name': '10D', 'suit': 'Diamonds', 'val': 10},
    49: {'name': 'JD', 'suit': 'Diamonds', 'val': 11},
    50: {'name': 'QD', 'suit': 'Diamonds', 'val': 12},
    51: {'name': 'KD', 'suit': 'Diamonds', 'val': 13},
}


handMap = {
    7: 'Royal Flush',
    6: 'Straight Flush',
    5: 'Three of a Kind',
    4: 'Straight',
    3: 'Flush',
    2: 'Pair',
    1: 'Qualifying High Card',
    0: 'Non Qualifying Hand'
}


strategyMap = {
    5: 'King High',
    4: 'Queen Ten',
    3: 'Queen Seven Four',
    2: 'Queen Six Four',
    1: 'Queen High',
    0: 'Blind'
}


def printDeck():
    for cardNum, cardVal in deck.items():
        for k1, v1 in cardVal.items():
            if k1 == 'name':
                print('Card is {} {}'.format(deck[cardNum][k1], cardNum))


def shuffleDeck():
    for x in xrange(0, 7):
        for y in xrange(0, len(deck)):
            z = randint(0, len(deck)-1)
            if (y != z):
                # print('y: {} z: {}'.format(deck[y], deck[z]) )
                # print('y: {} z: {}'.format(deck[y]['name'], deck[z]['name']))
                deck[y], deck[z] = deck[z], deck[y]


def printHand(hand):
    return hand[0]['name'] + " " + hand[1]['name'] + " " + hand[2]['name']


# score hand dict:
# score['has'] = True or False, if we have the hand we checked
# score['handval'] = (7..0, RoyalFlush=7 StraightFlush=6 ThreeofaKind=5
# Straight=4 Flush=3 Pair=2 Qual=1 NonQual=0
# score['1'] = Highest card value
# score['2'] = Second highest card value
# score['3'] = Third highest card value
def hasStraightFlush(hand):
    score = {}
    score['has'] = False
    if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit']:
        a = [hand[0]['val'], hand[1]['val'], hand[2]['val']]
        a.sort()
        # sorts ascending
        if a[0] + 1 == a[1]:
            if a[1] + 1 == a[2]:
                score['has'] = True
                score['handval'] = 6
                score['1'] = a[2]
                score['2'] = a[1]
                score['3'] = a[0]
        if a == [12, 13, 14]:
            score['handval'] = 7
        # [14, 2, 3] (A 2 3) is a straight
        if a == [2, 3, 14]:
            score['has'] = True
            score['handval'] = 6
            score['1'] = a[1]  # 3-high straight flush
            score['2'] = a[0]
            score['3'] = a[2]
    return score


def hasThreeofaKind(hand):
    score = {}
    score['has'] = False
    if hand[0]['val'] == hand[1]['val'] == hand[2]['val']:
        score['has'] = True
        score['handval'] = 5
        score['1'] = hand[0]['val']
        score['2'] = hand[1]['val']
        score['3'] = hand[2]['val']
    return score


def hasStraight(hand):
    score = {}
    score['has'] = False
    a = [hand[0]['val'], hand[1]['val'], hand[2]['val']]
    a.sort()
    # sorts ascending
    if a[0] + 1 == a[1]:
        if a[1] + 1 == a[2]:
            score['has'] = True
            score['handval'] = 4
            score['1'] = a[2]
            score['2'] = a[1]
            score['3'] = a[0]
    # [14, 2, 3] (A 2 3) is a straight too
    if a == [2, 3, 14]:
        score['has'] = True
        score['handval'] = 4
        score['1'] = a[1]
        score['2'] = a[0]
        score['3'] = a[2]
    return score


def hasFlush(hand):
    score = {}
    score['has'] = False
    if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit']:
        a = [hand[0]['val'], hand[1]['val'], hand[2]['val']]
        a.sort()
        score['has'] = True
        score['handval'] = 3
        score['1'] = a[2]
        score['2'] = a[1]
        score['3'] = a[0]
    return score


def hasPair(hand):
    score = {}
    score['has'] = False
    if hand[0]['val'] == hand[1]['val']:
        score['has'] = True
        score['handval'] = 2
        score['1'] = hand[0]['val']
        score['2'] = hand[1]['val']
        score['3'] = hand[2]['val']
    elif hand[0]['val'] == hand[2]['val']:
        score['has'] = True
        score['handval'] = 2
        score['1'] = hand[0]['val']
        score['2'] = hand[2]['val']
        score['3'] = hand[1]['val']
    elif hand[1]['val'] == hand[2]['val']:
        score['has'] = True
        score['handval'] = 2
        score['1'] = hand[1]['val']
        score['2'] = hand[2]['val']
        score['3'] = hand[0]['val']
    return score


def hasQualifyingHighCard(hand):
    score = {}
    score['has'] = False
    a = [hand[0]['val'], hand[1]['val'], hand[2]['val']]
    a.sort()
    if a[2] >= 12:
        score['has'] = True
        score['handval'] = 1
        score['1'] = a[2]
        score['2'] = a[1]
        score['3'] = a[0]
    return score


def hasKingHigh(hand):
    score = {}
    score['has'] = False
    a = [hand[0]['val'], hand[1]['val'], hand[2]['val']]
    a.sort()
    if a[2] >= 13:
        score['has'] = True
        score['handval'] = 1
        score['1'] = a[2]
        score['2'] = a[1]
        score['3'] = a[0]
    return score


def hasQueenTen(hand):
    score = {}
    score['has'] = False
    a = [hand[0]['val'], hand[1]['val'], hand[2]['val']]
    a.sort()
    if a[2] > 12:
        score['has'] = True
    elif a[2] == 12:
        if a[1] >= 10:
            score['has'] = True

    if score['has']:
        score['handval'] = 1
        score['1'] = a[2]
        score['2'] = a[1]
        score['3'] = a[0]
    return score


def hasQueenSevenFour(hand):
    score = {}
    score['has'] = False
    a = [hand[0]['val'], hand[1]['val'], hand[2]['val']]
    a.sort()
    if a[2] > 12:
        score['has'] = True
    elif a[2] == 12:
        if a[1] > 7:
            score['has'] = True
        elif a[1] == 7:
            if a[0] >= 4:
                score['has'] = True
    if score['has']:
        score['handval'] = 1
        score['1'] = a[2]
        score['2'] = a[1]
        score['3'] = a[0]
    return score


def hasQueenSixFour(hand):
    score = {}
    score['has'] = False
    a = [hand[0]['val'], hand[1]['val'], hand[2]['val']]
    a.sort()
    if a[2] > 12:
        score['has'] = True
    elif a[2] == 12:
        if a[1] > 7:
            score['has'] = True
        elif a[1] == 6:
            if a[0] >= 4:
                score['has'] = True
    if score['has']:
        score['handval'] = 1
        score['1'] = a[2]
        score['2'] = a[1]
        score['3'] = a[0]
    return score


def playable(hand, strategy):
    # Assumes strategies are for certain thresholds non-pairplus hands
    # 0=blind, 1=Q, 2=Q64, 3=Q74, 4=Q10, 5=K
    # print('folds testing {} strategy {}'.format(hand, strategy))

    if strategy == 0:
        # Play blind
        return True

    # Set name = 'nobody' so we don't print the hand while testing playability
    x = evaluateHand(hand, 'nobody')
    if x['handval'] >= 2:
        # Always play a pair
        return True

    if strategy == 5:
        # King high required
        x = hasKingHigh(hand)
        if x['has']:
            return True
    if strategy == 4:
        # Queen 10 anything
        x = hasQueenTen(hand)
        if x['has']:
            return True
    if strategy == 3:
        # Queen 7 4
        x = hasQueenSevenFour(hand)
        if x['has']:
            return True
    if strategy == 2:
        # Queen 6 4
        x = hasQueenSixFour(hand)
        if x['has']:
            return True
    if strategy == 1:
        # Queen high, qualifying only, dealer strategy
        x = hasQualifyingHighCard(hand)
        if x['has']:
            return True

    return False


def printEvaluation(name, handText, hand):
    if name != 'nobody':
        print('{} has a {}! {}'.format(name, handText, hand))


def evaluateHand(hand, name):
    x = {}
    x['has'] = 0
    x = hasStraightFlush(hand)
    if x['has']:
        if x['handval'] == 7:
            printEvaluation(name, handMap[7], printHand(hand))
        else:
            printEvaluation(name, handMap[6], printHand(hand))
        return x
    x = hasThreeofaKind(hand)
    if x['has']:
        printEvaluation(name, handMap[5], printHand(hand))
        return x
    x = hasStraight(hand)
    if x['has']:
        printEvaluation(name, handMap[4], printHand(hand))
        return x
    x = hasFlush(hand)
    if x['has']:
        printEvaluation(name, handMap[3], printHand(hand))
        return x
    x = hasPair(hand)
    if x['has']:
        printEvaluation(name, handMap[2], printHand(hand))
        return hasPair(hand)
    x = hasQualifyingHighCard(hand)
    if x['has']:
        printEvaluation(name, handMap[1], printHand(hand))
        return x
    printEvaluation(name, handMap[0], printHand(hand))
    x['handval'] = 0
    return x


def checkAntePlay(player, dealer, betType, betAmt):
    # returns (Text, Value)
    # Text describes result and net gain/lossfor this bet
    # Value = betAmt for push, betAmt * 2 for win, 0 for loss

    anteBonus = 0
    # StraightFlush(7, 6) = 5 x betAmt
    # ThreeofaKind(5) = 4 x betAmt
    # Straight(4) = 1 x betAmt
    paytable = {7: 5, 6: 5, 5: 4, 4: 1}
    if betType == 'Ante' and player['handval'] >= 4:
        anteBonus = paytable[player['handval']] * betAmt
        print('Player wins Ante bonus! ({})'.format(anteBonus))

    win = betAmt * 2 + anteBonus
    loss = 0 + anteBonus
    if dealer['handval'] == 0:
        if betType == 'Ante':
            return('Dealer doesn\'t qualify, player wins Ante bet (+{})'.
                   format(betAmt), win)
        elif betType == 'Play':
            return('Dealer doesn\'t qualify, player pushes Play bet (0)',
                   betAmt)

    if player['handval'] > dealer['handval']:
        return('Player wins {} bet (+{})'.format(betType, betAmt), win)
    elif player['handval'] == dealer['handval']:
        if player['1'] > dealer['1']:
            return('Player wins {} bet (+{})'.format(betType, betAmt), win)
        elif player['1'] == dealer['1']:
            if player['2'] > dealer['2']:
                return('Player wins {} bet (+{})'.format(betType, betAmt), win)
            elif player['2'] == dealer['2']:
                if player['3'] > dealer['3']:
                    return('Player wins {} bet (+{})'.format(betType, betAmt),
                           win)
                elif player['3'] == dealer['3']:
                    # dealer wins 3-card pushes
                    return('Player loses {} bet (3-card push) ({})'.format(
                           betType, -betAmt), loss)
                else:
                    return('Player loses {} bet ({})'.format(
                           betType, -betAmt), loss)
            else:
                return('Player loses {} bet ({})'.format(betType, -betAmt),
                       loss)
        else:
            return('Player loses {} bet ({})'.format(betType, -betAmt), loss)
    else:
        return('Player loses {} bet ({})'.format(betType, -betAmt), loss)


def checkPairPlus(player, table, betAmt):
    # returns (Text, Value)
    # Text describes result and net gain/lossfor this bet
    # Value = betAmt * paytable['handval'] for win, 0 for loss
    paytable = {
        1: {7: 40, 6: 40, 5: 30, 4: 6, 3: 4, 2: 1, 1: 0, 0: 0},
        2: {7: 35, 6: 35, 5: 33, 4: 6, 3: 4, 2: 1, 1: 0, 0: 0},
        3: {7: 40, 6: 40, 5: 30, 4: 6, 3: 3, 2: 1, 1: 0, 0: 0},
    }

    if player['handval'] >= 2:
        win = paytable[table][player['handval']] * betAmt + betAmt
        return ('Player wins PairPlus bet (+{})'.format(win),
                win)
    else:
        return ('Player loses PairPlus bet ({})'.format(-betAmt), 0)

stats = {
    # a=anteBet p=playBet pp=pairplusBet t=totalMoney s=strategy:
    # 0=blind, 1=Q, 2=Q10, 3=Q74, 4=Q64, 5=K
    # g=gamesPlayed w=win l=loss pu=push f=fold al=alive
    # (7..0) = num games with that handval
    1: {'a': 10, 'p': 10, 'pp': 10, 't': 0,
        's': 0, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
        7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    2: {'a': 20, 'p': 20, 'pp': 20, 't': 0,
        's': 3, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
        7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    3: {'a': 10, 'p': 10, 'pp': 5, 't': 0,
        's': 4, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
        7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    4: {'a': 10, 'p': 10, 'pp': 5, 't': 0,
        's': 3, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
        7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    5: {'a': 15, 'p': 15, 'pp': 10, 't': 0,
        's': 4, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
        7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    6: {'a': 15, 'p': 15, 'pp': 10, 't': 0,
        's': 1, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
        7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    7: {'a': 15, 'p': 15, 'pp': 5, 't': 0,
        's': 2, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
        7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    8: {'a': 15, 'p': 15, 'pp': 15, 't': 0,
        's': 3, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
        7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    9: {'a': 50, 'p': 50, 'pp': 10, 't': 0,
        's': 5, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
        7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    10: {'a': 50, 'p': 50, 'pp': 10, 't': 0,
         's': 3, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
         7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    11: {'a': 10, 'p': 10, 'pp': 20, 't': 0,
         's': 3, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
         7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    12: {'a': 10, 'p': 10, 'pp': 20, 't': 0,
         's': 4, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
         7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    13: {'a': 10, 'p': 10, 'pp': 5, 't': 0,
         's': 3, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
         7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    14: {'a': 20, 'p': 20, 'pp': 20, 't': 0,
         's': 3, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
         7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    15: {'a': 40, 'p': 40, 'pp': 40, 't': 0,
         's': 4, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
         7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    16: {'a': 40, 'p': 40, 'pp': 20, 't': 0,
         's': 3, 'g': 0, 'w': 0, 'l': 0, 'pu': 0, 'f': 0, 'al': 1,
         7: 3, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
}

# everyone starts with the same amount.  track it here because
# stats[player]['t'] is a running total and we need to remember startAmt
startAmt = 1000
for player in stats.keys():
    stats[player]['t'] = startAmt

games = 10000
game = 0

while game < games:
    playTheGame = False
    # if someone is alive, let's play
    for player in stats.keys():
        if stats[player]['al'] == 1:
            playTheGame = True
            break

    if playTheGame:
        game += 1
        print('Game number {}'.format(game))

        shuffleDeck()
        # printDeck()

        # last player is dealer, max = 17
        numPlayers = 17

        # pairplus pay table
        ppTable = 3

        # deal $numPlayers hands
        c = 0  # count of cards
        hands = {}
        for x in xrange(1, numPlayers+1):
            hands[x] = {}
            for y in xrange(0, 3):
                hands[x][y] = deck[c]
                c = c + 1

        dealer = evaluateHand(hands[numPlayers], 'Dealer')
        print('')

        for player in hands.keys():
            if player != numPlayers:      # if we're not the dealer
                if stats[player]['al'] == 1:
                    stats[player]['g'] += 1

                    start = stats[player]['t']
                    print('Player {} starts with {} playing strategy {}'.format(player, stats[player]['t'], strategyMap[stats[player]['s']]))
                    print('Player places ante bet ({}) pairplus bet ({})'.format(stats[player]['a'], stats[player]['pp']))
                    stats[player]['t'] -= stats[player]['a']
                    x = evaluateHand(hands[player], 'Player {}'.format(player))
                    stats[player][x['handval']] += 1

                    if playable(hands[player], stats[player]['s']):

                        print('Player places play bet ({})'.format(stats[player]['p']))
                        print('Player playing {} vs Dealer {}'.format(printHand(hands[player]), printHand(hands[numPlayers])))
                        anteText, anteVal = checkAntePlay(x, dealer, 'Ante', stats[player]['a'])
                        print('{}'.format(anteText))
                        stats[player]['t'] += anteVal

                        stats[player]['t'] -= stats[player]['p']
                        playText, playVal = checkAntePlay(x, dealer, 'Play', stats[player]['p'])
                        print('{}'.format(playText))
                        stats[player]['t'] += playVal

                        stats[player]['t'] -= stats[player]['pp']
                        pairplusText, pairplusVal = checkPairPlus(x, ppTable, stats[player]['pp'])
                        print('{}'.format(pairplusText))
                        stats[player]['t'] += pairplusVal

                    else:
                        # Fold, forfeit pairplus bet
                        print('Player folds, hand {} strategy {}'.format(printHand(hands[player]), strategyMap[stats[player]['s']]))
                        stats[player]['t'] -= stats[player]['pp']
                        # stats[player]['f'] += 1

                    end = stats[player]['t']
                    res = end - start
                    if res > 0:
                        stats[player]['w'] += 1
                        res = '+' + str(res)
                    elif res == -(stats[player]['a'] + stats[player]['pp']):
                        stats[player]['f'] += 1
                    elif res < 0:
                        stats[player]['l'] += 1
                    else:
                        stats[player]['pu'] += 1

                    # if we don't have enough money to play more, set alive=0
                    if stats[player]['t'] < stats[player]['a'] + stats[player]['p'] + stats[player]['pp']:
                        stats[player]['al'] = 0

                    print('Player {} started with {} and ended with {} ({})'.format(player, start, end, res))
                    print('')

        print('Game number {} done!'.format(game))
    else:
        print('Game over after {} games!'.format(game))
        break

for player in stats.keys():
    print('Player {} played {} of {} games ({}%) and ended with {} ({}% house edge)'.format(player, stats[player]['g'], (game), (stats[player]['g'] / (game) * 100), stats[player]['t'], (stats[player]['t'] - startAmt) / -stats[player]['g']))
    print('Player {} played strategy {}, Ante/Play {} PairPlus {} ({}/hand)'.format(player, strategyMap[stats[player]['s']], stats[player]['a'], stats[player]['pp'], (2 * stats[player]['a'] + stats[player]['pp'])))
    for k in handMap.keys():
        print('Player {} had {} x {} ({}%)'.format(player, stats[player][k], handMap[k], (stats[player][k] / stats[player]['g']) * 100))
    print('Player {} had {} wins ({}%), {} losses ({}%), {} pushes ({}%), and {} folds ({}%)'.format(player, stats[player]['w'], (stats[player]['w'] / stats[player]['g'] * 100), stats[player]['l'], (stats[player]['l'] / stats[player]['g'] * 100), stats[player]['pu'], (stats[player]['pu'] / stats[player]['g'] * 100), stats[player]['f'], (stats[player]['f'] / stats[player]['g'] * 100)))
    print('')

# testHand1 = {
#   0: {'name':'AS', 'suit':'Spades', 'val':14},
#   1: {'name':'QS', 'suit':'Spades', 'val':12},
#   2: {'name':'KS', 'suit':'Spades', 'val':13},
# }
# testHand2 = {
#   0: {'name':'6D', 'suit':'Diamonds', 'val':6},
#   1: {'name':'8D', 'suit':'Diamonds', 'val':8},
#   2: {'name':'7D', 'suit':'Diamonds', 'val':7},
# }
# testHand3 = {
#   0: {'name':'2C', 'suit':'Clubs', 'val':2},
#   1: {'name':'2S', 'suit':'Spades', 'val':2},
#   2: {'name':'2H', 'suit':'Hearts', 'val':2},
# }
# testHand4 = {
#   0: {'name':'QC', 'suit':'Clubs', 'val':12},
#   1: {'name':'KS', 'suit':'Spades', 'val':13},
#   2: {'name':'AH', 'suit':'Hearts', 'val':14},
# }
# testHand5 = {
#   0: {'name':'7H', 'suit':'Hearts', 'val':7},
#   1: {'name':'2H', 'suit':'Hearts', 'val':2},
#   2: {'name':'3H', 'suit':'Hearts', 'val':3},
# }
# testHand6 = {
#   0: {'name':'7H', 'suit':'Hearts', 'val':7},
#   1: {'name':'5H', 'suit':'Hearts', 'val':5},
#   2: {'name':'5S', 'suit':'Spades', 'val':5},
# }
# testHand7 = {
#   0: {'name':'QH', 'suit':'Hearts', 'val':12},
#   1: {'name':'5H', 'suit':'Hearts', 'val':5},
#   2: {'name':'2S', 'suit':'Spades', 'val':2},
# }
# testHand8 = {
#   0: deck[3],
#   1: deck[5],
#   2: deck[6],
# }
# print('\n')
# x = hasStraightFlush(testHand1)
# print('has str flush? {} {} {} {}'.format(x['has'],x['1'],x['handval'], printHand(testHand1)))
# x = hasStraightFlush(testHand2)
# print('has str flush? {} {} {} {}'.format(x['has'],x['1'],x['handval'], printHand(testHand2)))
# x = hasThreeofaKind(testHand3)
# print('has 3 kind? {} {} {}'.format(x['has'],x['1'], printHand(testHand3)))
# x = hasStraight(testHand4)
# print('has str ? {} {} {}'.format(x['has'],x['1'], printHand(testHand4)))
# x = hasFlush(testHand5)
# print('has flush ? {} {} {}'.format(x['has'],x['1'], printHand(testHand5)))
# x = hasPair(testHand6)
# print('has pair ? {} {} {}'.format(x['has'],x['1'], printHand(testHand6)))
# x = hasQualifyingHighCard(testHand7)
# print('has qual ? {} {} {}'.format(x['has'],x['1'], printHand(testHand7)))
# print('\n')
#
# printHand(testHand1)
# zz = evaluateHand(testHand1, 'Test1')
