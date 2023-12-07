hands  = [i.strip() for i in open('7data.txt', 'r').readlines()]
hands = [i.split(' ') for i in hands]
cardsymbols = 'AKQJT987654321'
cardsymbols = [i for i in cardsymbols]
handtypes = [[] for i in range(7)]
for i in hands:
    fullhouse = [False, False]
    hand = i[0]
    doublelist = []
    priorityflag = 10
    for symbol in cardsymbols:
        print(hand, ' ', symbol, '', fullhouse)
        if hand.count(symbol) == 5:
            hands.remove(i)
            handtypes[0].append(i)
            priorityflag = 0
        elif hand.count(symbol) == 4 and priorityflag > 0:
            hands.remove(i)
            handtypes[1].append(i)
            priorityflag = 1
        elif hand.count(symbol) == 3 and priorityflag > 1:
            fullhouse[0] = True
        elif hand.count(symbol) == 2 and priorityflag > 1:
            if symbol not in doublelist: doublelist.append(symbol)
            fullhouse[1] = True
    if (fullhouse == (True, True)):
            print('full house')
            hands.remove(i)
            handtypes[2].append(i)
            priorityflag = 2
    if (fullhouse == True, False) and priorityflag > 2:
        #three of a kind, occurs if the three similiar cards, but not the two similiar cards, were found
        hands.remove(i)
        handtypes[3].append(i)
        priorityflag = 3
    if len(doublelist)>2 and priorityflag >3:
        hands.remove(i)
        handtypes[4].append(i)
        priorityflag = 4
    if priorityflag == 10:
        hands.remove(i)
        handtypes[6].append(i)



        
print(handtypes)
