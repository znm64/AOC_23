lines = [i.strip() for i in open('13data.txt', 'r')]
blocks = []
current = []
for i in lines:
    if i != '':
        current.append(i)
    else:
        blocks.append(current)
        current = []
blocks.append(current)

def getcol(x, block):
    return [i[x] for i in block]

def horsymcheck(block, x):
    x_offset = 0
    left = []
    right = []
    
    if x > len(block[0])//2:
        while x+x_offset <= len(block[0]):
            left.append(getcol(x-x_offset, block))
            right.append(getcol(x+x_offset-1, block))
            x_offset += 1
    else:
        while x-x_offset >= 0 and x+x_offset < len(block[0]):
            left.append(getcol(x-x_offset, block))
            right.append(getcol(x+x_offset-1, block))
            x_offset += 1
    return (left == right)

def vertsymcheck(block, y):
    y_offset = 0
    up = []
    down = []
    if y > len(block)//2:
        while y+y_offset < len(block):
            up.append(block[y-y_offset])
            down.append(block[y+y_offset-1])
            y_offset += 1
    else:
        while y-y_offset >= 0 and y+y_offset <= len(block[0]):
            up.append(block[y-y_offset])
            down.append(block[y+y_offset-1])
            y_offset += 1
    return (up == down)

xlist = []
ylist = []
for i in blocks:
    for x in range(len(i[0])):
        if (horsymcheck(i, x)):
            xlist.append(x)
            print('hor', x)
    for y in range(len(i)):
        if (vertsymcheck(i, y)): 
            ylist.append(y)
            print('vert', y)
print(xlist, ylist)
print(sum(ylist)*100 + sum(xlist))