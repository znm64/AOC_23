import math
#part 1
raw  = [i.strip() for i in open('8data.txt', 'r').readlines()]
direction = raw[0]
map = []
for i in raw[2:]:
    running = ''
    for i2 in i:
        if i2.isalpha(): running+=i2
    map.append(running)
mapdic = {}
for i in map: mapdic[i[:3]] = [i[3:6], i[6:]]

currentpos = 'AAA'
dircount = 0
movecount = 0
while currentpos != 'ZZZ':
    currentdirection = direction[(dircount % len(direction))]
    currentdirection = (1 if currentdirection == 'R' else 0)
    dircount += 1
    movecount += 1
    currentpos = mapdic[currentpos][currentdirection]
print(movecount)

#part 2
raw  = [i.strip() for i in open('8data.txt', 'r').readlines()]
direction = raw[0]
map = []
for i in raw[2:]:
    running = ''
    for i2 in i:
        if i2.isalnum():running+=i2
    map.append(running)
mapdic = {}
for i in map:mapdic[i[:3]] = [i[3:6], i[6:]]

currentpos = []
for i in mapdic:
    if i[2] == 'A': currentpos.append(i)
dircount = 0
movements = 0
lcmreg = [0 for i in currentpos]
finish = []
final = 1
while (0 in lcmreg):
    currentdirection = (1 if direction[(movements % len(direction))] == 'R' else 0)
    movements += 1
    for count, i in enumerate(currentpos):
        currentpos[count] = mapdic[i][currentdirection]
        if i[2] == 'Z': lcmreg[count] = 1;final = math.lcm(final, movements-1)
print(final)