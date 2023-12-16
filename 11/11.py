'''lines = [i.strip() for i in open('11data.txt', 'r').readlines()]
def rowcheck(lines):
    moveover = False
    for count, i in enumerate(lines):
        if not moveover:
            if not '#' in i:
                lines.insert(count, '.'*len(lines[0]))
                moveover = True
        else:
            moveover = False
    return lines
lines = rowcheck(lines)

def getcol(x):
    return [i[x] for i in lines]

def colinsert(lines, x):
    #part 1 original
    lines = [i[:x]+'.'+i[x:] for i in lines]
    return lines

def colcheck(lines):
    moveover = False
    inserts = 0
    for count in range(len(lines[0])):
        if not moveover:
            if not '#' in getcol(count):
                lines = colinsert(lines, count+inserts)
                inserts += 1
                moveover = True
        else:
            moveover = False
    return lines
lines = colcheck(lines)
galaxies = []
for y, row in enumerate(lines):
    for x, i in enumerate(row):

        if i == '#':galaxies.append([x, y])
print(galaxies)
sum = 0
for base in galaxies:
    for destination in galaxies:
        if base != destination:
            sum += abs(destination[0] - base[0])+abs(destination[1]-base[1])
print(sum//2)
'''
#part2
lines = [i.strip() for i in open('11data.txt', 'r').readlines()]
def rowcheck(lines):
    moveover = False
    for count, i in enumerate(lines):
        if not moveover:
            if not '#' in i:
                lines.insert(count, '*'*len(lines[0]))
                moveover = True
        else:
            moveover = False
    return lines
lines = rowcheck(lines)

def getcol(x):
    return [i[x] for i in lines]

def colinsert(lines, x):
    #part 1 original
    lines = [i[:x]+'*'+i[x:] for i in lines]
    return lines

def colcheck(lines):
    moveover = False
    inserts = 0
    for count in range(len(lines[0])):
        if not moveover:
            if not '#' in getcol(count):
                lines = colinsert(lines, count+inserts)
                inserts += 1
                moveover = True
        else:
            moveover = False
    return lines
lines = colcheck(lines)
galaxies = []
for y, row in enumerate(lines):
    for x, i in enumerate(row):
        if i == '#':galaxies.append([x, y])
for i in lines:
    print(i)
print(galaxies)
final = 0
for base in galaxies:
    for destination in galaxies:
        location = base
        horizontalpath= []
        verticalpath= []
        if location[0] != destination[0]:
            horizontalpath = destination[0] - location[0]
            if horizontalpath > 0: horizontalpath = lines[location[1]][location[0]+1:location[0]+horizontalpath+1]
            else:horizontalpath = lines[location[1]][location[0]+horizontalpath:location[0]]
            
        if location[1] != destination[1]:
            verticalpath = destination[1] - location[1]
            if verticalpath > 0: verticalpath = ''.join(getcol(location[0])[location[1]+1:location[1]+verticalpath+1])
            else: verticalpath = ''.join(getcol(location[0])[location[1]+verticalpath:location[1]])
        print(location, destination)
        print(horizontalpath, ',', verticalpath)
        if horizontalpath == []: horizontalpath = ''
        if verticalpath == []: verticalpath = ''
        a = ([10**6 if i == '*' else 1 for i in horizontalpath+verticalpath])
        print('sum:', sum(a))
        final+=sum(a) 
print(final//2)
