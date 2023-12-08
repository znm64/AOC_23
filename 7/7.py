#part 1

'''from operator import itemgetter, attrgetter
hands  = [i.strip() for i in open('7data.txt', 'r').readlines()]
hands = [i.split(' ') for i in hands]
cardsymbols = 'AKQJT98765432'
cardsymbols = [i for i in cardsymbols]
handtypes = [[] for i in range(7)]

def calcvalue(hand):
    total = 0
    for count, i in enumerate(''.join(reversed(hand))):
        total += ((13-cardsymbols.index(i)) * (13**(count)))
    return total


for i in hands:
    fullhouse = [False, False]
    hand = i[0]
    doublelist = []
    priorityflag = 10
    for symbol in cardsymbols:
        #print(hand, ' ', symbol, '', fullhouse)
        if hand.count(symbol) == 5:
            #five of a kind
            handtypes[0].append(i)
            priorityflag = 0
        elif hand.count(symbol) == 4 and priorityflag > 0:
            #four of a kind
            handtypes[1].append(i)
            priorityflag = 1
        elif hand.count(symbol) == 3 and priorityflag > 1:
            #finding groups of three for three of a kind/full house
            fullhouse[0] = True
        elif hand.count(symbol) == 2 and priorityflag > 1:
            #finding groups of two for three of a kind/full house
            if symbol not in doublelist: doublelist.append(symbol)
            fullhouse[1] = True
    if (fullhouse == [True, True]) and priorityflag > 1:
        #full house
        handtypes[2].append(i)
        priorityflag = 2
    elif (fullhouse == [True, False]) and priorityflag > 2:
        #three of a kind
        handtypes[3].append(i)
        priorityflag = 3
    elif len(doublelist)>=2 and priorityflag >3:
        #two pair
        handtypes[4].append(i)
        priorityflag = 4
    elif len(doublelist) == 1 and priorityflag >4:
        #one pair
        handtypes[5].append(i)
        priorityflag = 5
    elif priorityflag == 10:
        handtypes[6].append(i)
        priorityflag = 6
    handtypes[priorityflag][-1].append(calcvalue(handtypes[priorityflag][-1][0]))
final = []
for i in handtypes.__reversed__():  
    for each in sorted(i, key=lambda x: x[2]):
        final.append(each[:2])
print(final)
total = 0
for count, i in enumerate(final):
    total += int(i[1])*(count+1)
print(total)'''

#part 2
#doesn't quite work, but close
#need to count how many jokers were used, then stop them from being reused
#use this test case: https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/
from operator import itemgetter, attrgetter
hands  = [i.strip() for i in open('7data.txt', 'r').readlines()]
hands = [i.split(' ') for i in hands]
cardsymbols = 'AKQT98765432J'
cardsymbols = [i for i in cardsymbols]
handtypes = [[] for i in range(7)]

def calcvalue(hand):
    total = 0
    for count, i in enumerate(''.join(reversed(hand))):
        total += ((13-cardsymbols.index(i)) * (13**(count)))
    return total


for i in hands:
    fullhouse = [False, False]
    jokersused = [0, 0]
    #no. of jokers used, and test priority
    hand = i[0]
    doublelist = []
    priorityflag = 10
    test = (hand == 'JJJJ2')
    for symbol in cardsymbols:
        #print(hand, ' ', symbol, '', fullhouse)
        if (hand.count(symbol) + hand.count('J')) == 5 and priorityflag != 0:
            #five of a kind
            priorityflag = 0
            if test:print('five')
        elif (hand.count(symbol) + hand.count('J')) == 4 and priorityflag > 1:
            #four of a kind
            priorityflag = 1
            if test:print('four')
        if (hand.count(symbol) + hand.count('J')) == 3 and priorityflag > 1:
            #finding groups of three for three of a kind/full house
            fullhouse[0] = True
        if (hand.count(symbol) + hand.count('J')) == 2 and priorityflag > 1:
            #finding groups of two for three of a kind/full house
            if symbol not in doublelist: 
                doublelist.append(symbol)
            fullhouse[1] = True
    if (fullhouse == [True, True]) and priorityflag > 1:
        #full house
        priorityflag = 2
        if test:print('fullhouse')
    elif (fullhouse == [True, False]) and priorityflag > 2:
        #three of a kind
        priorityflag = 3
        if test:print('threekind')
    elif len(doublelist)>=2 and priorityflag >3:
        #two pair
        priorityflag = 4
        if test:print('twopair ', doublelist)
    elif len(doublelist) == 1 and priorityflag >4:
        #one pair
        priorityflag = 5
        if test:print('onepair')
    elif priorityflag == 10:
        priorityflag = 6
    handtypes[priorityflag].append(i)

    handtypes[priorityflag][-1].append(calcvalue(handtypes[priorityflag][-1][0]))
print(handtypes)
final = []
for i in handtypes.__reversed__():  
    for each in sorted(i, key=lambda x: x[2]):
        final.append(each[:2])
total = 0
for count, i in enumerate(final):
    total += int(i[1])*(count+1)
print(total)