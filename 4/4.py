#part1
'''
raw = [i.strip() for i in open('4data.txt', 'r').readlines()]

def getnums(raw):
    lines = []
    current = ''
    for i in raw:
        current = (i[i.index(':')+1:].strip())
        current = current.split('|')
        for count, i in enumerate(current):
            current[count] = i.split(' ')
        for count, i in enumerate(current):
            a = [int(x) for x in i if len(x)!=0]
            current[count] = a
        lines.append(current)
    return lines
allnums = (getnums(raw))

#calculate total score
scores = []
for card in allnums:
    score = 0
    for eachnum in card[0]:
        if eachnum in card[1]:
            score = (score*2 if score > 0 else 1)
    scores.append(score)
print(scores)
print(sum(scores))'''

#part2

raw = [i.strip() for i in open('4data.txt', 'r').readlines()]

def getnums(raw):
    lines = []
    current = ''
    for i in raw:
        current = (i[i.index(':')+1:].strip())
        current = current.split('|')
        for count, i in enumerate(current):
            current[count] = i.split(' ')
        for count, i in enumerate(current):
            a = [int(x) for x in i if len(x)!=0]
            current[count] = a
        lines.append(current)
    return lines
allnums = (getnums(raw))

cards = [i for i in range(len(allnums))]
print(cards.count(1))
#goes to the first card in cards, finds score, adds the new cards
final = 0
while sum(cards) != 0:
    cards.sort()
    cardnum = cards.pop(0)
    card = allnums[cardnum]
    repeats = cards.count(cardnum)
    print(cards)
    print('cardnum', cardnum)
    print('repeats', repeats)
    final += repeats+1
    cards = cards[repeats:]
    score = 0
    for eachnum in card[0]:
        if eachnum in card[1]:
            score += 1
    if score>0:
        newcards = [i for i in range(cardnum+1, cardnum+score+1)]
        for i in newcards:
            for count in range(repeats+1):
                cards.append(i)
        #print(newcards)
print(final)

