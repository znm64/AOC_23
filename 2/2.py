#part1
raw = open('2data.txt', 'r').readlines()
def dataprocess(raw):
    lines = []
    for i in raw:
        lines.append(i[i.index(':')+1:].strip())
    for i in range(len(lines)):
        lines[i] = lines[i].replace('; ', ', ')
        lines[i] = lines[i].split(', ')        
    return lines
lines = (dataprocess(raw))
total = 0
validlist = [True for i in range(len(lines))]
for count1, i1 in enumerate(lines):
    print('NEW GAME')
    for count2, i2 in enumerate(i1):
        currentnum = ''
        print(i2)
        for i3 in i2:
            if i3.isdigit():
                currentnum += i3
        currentnum = int(currentnum)
        print(currentnum)
        if ('red' in i2 and currentnum > 12) or ('green' in i2 and currentnum > 13) or ('blue' in i2 and currentnum > 14):
            validlist[count1] = False
print(validlist)
for count, i in enumerate(validlist):
    if i == True:
        total += count+1
print(total)
#part2
raw = open('data.txt', 'r').readlines()
def dataprocess(raw):
    lines = []
    for i in raw:
        lines.append(i[i.index(':')+1:].strip())
    for i in range(len(lines)):
        lines[i] = lines[i].replace('; ', ', ')
        lines[i] = lines[i].split(', ')        
    return lines
lines = (dataprocess(raw))
total = 0
powerlist = [0 for i in range(len(lines))]
for count1, i1 in enumerate(lines):
    print('NEW GAME')
    redmin, greenmin, bluemin = -1,-1,-1
    for count2, i2 in enumerate(i1):
        currentnum = ''
        print(i2)
        for i3 in i2:
            if i3.isdigit():
                currentnum += i3
        currentnum = int(currentnum)
        if ('red' in i2):
            if currentnum > redmin or redmin == -1:
                redmin = currentnum
                print(redmin)
        elif ('green' in i2):
            if currentnum > greenmin or greenmin == -1:
                greenmin = currentnum
                print(greenmin)
        elif ('blue' in i2):
            if currentnum > bluemin or bluemin == -1:
                bluemin = currentnum
                print(bluemin)

    power = bluemin*redmin*greenmin
    powerlist[count1] = power
        

print(powerlist)
print(sum(powerlist))