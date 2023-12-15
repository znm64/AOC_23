lines = [i.strip() for i in open('11data.txt', 'r').readlines()]
print(lines)
def rowcheck(lines):
    moveover = False
    for count, i in enumerate(lines):
        if not moveover:
            if not '#' in i:
                lines.insert(count, lines[count])
                print('inserted at', count)
                moveover = True
        else:
            moveover = False
    return lines
lines = rowcheck(lines)
for i in lines:
    print(i)

def getcol(x):
    return [i[x] for i in lines]

def colinsert(lines, x):
    lines = [i[:x]+'.'+i[x+1:] for i in lines]
    return lines

def colcheck(lines):
    moveover = False
    for count in range(len(lines[0])):
        if not moveover:
            if not '#' in getcol(count):
                lines = colinsert(lines, count)
                print('inserted at', count)

                moveover = True
        else:
            moveover = False
    return lines
lines = colcheck(lines)
print(lines)
for y, col in enumerate(lines):
    for x, element in enumerate(col):
        print(element)