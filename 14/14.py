'''lines = [list(i2) for i2 in [i.strip() for i in open('15data.txt', 'r').readlines()]]
def northslide(lines):
    circular = []
    for y, row in enumerate(lines):
        for x, element in enumerate(row):
            if element == 'O':
                circular.append([x, y])
    for i in circular:
        xpos = i[0]
        ypos = i[1]
        while ypos > 0:
            if lines[ypos-1][xpos] != '#' and lines[ypos-1][xpos] != 'O':
                lines[ypos][xpos], lines[ypos-1][xpos], ypos = '.', 'O', ypos-1
            else:
                break
    return lines
def stresscalc(lines):
    total = 0
    for y, row in enumerate(lines):
        mult = len(lines)-y
        for item in row:
            if item == 'O':
                total += mult
    return total
lines = northslide(lines)
print(stresscalc(lines))'''
#part 2
#sort function to allow for the circular list to be sorted
def hor_sort(i):
    return i[0]
def vert_sort(i):
    return i[1]
global history
history = []

lines = [list(i2) for i2 in [i.strip() for i in open('14data.txt', 'r').readlines()]]
def slide(lines, dir):
    #dir is an int - 0:north, 1:east, 2:south, 3:west
    circular = []
    for y, row in enumerate(lines):
        for x, element in enumerate(row):
            if element == 'O':
                circular.append([x, y])
    if dir == 0 or dir == 2:
       #N and S directions
        if dir == 2:
            dir = -1
            circular.sort(key=vert_sort, reverse=True)
        else:
            dir = 1
            circular.sort(key=vert_sort)
        for i in circular:
            xpos = i[0]
            ypos = i[1]
            while (ypos > 0 if dir == 1 else ypos < len(lines)-1):
                if lines[ypos-dir][xpos] != '#' and lines[ypos-dir][xpos] != 'O':
                    lines[ypos][xpos], lines[ypos-dir][xpos], ypos = '.', 'O', ypos-dir
                else:
                    break
        if dir == 1:history.append(circular)
    else:
        #E and W directions
        if dir == 3:
            dir = -1
            circular.sort(key=hor_sort)
        else:
            dir = 1
            circular.sort(key=hor_sort, reverse=True)
        for i in circular:
            xpos = i[0]
            ypos = i[1]
            while (xpos > 0 if dir == -1 else xpos < len(lines[0])-1):
                if lines[ypos][xpos+dir] == '.':
                    lines[ypos][xpos], lines[ypos][xpos+dir], xpos = '.', 'O', xpos+dir
                else:
                    break
    
    return lines

def stresscalc(lines):
    total = 0
    for y, row in enumerate(lines):
        mult = len(lines)-y
        for item in row:
            if item == 'O':
                total += mult
    return total
dirs = [0,3,2,1]
for i in range(1000000000):
    for i in dirs:
        lines = slide(lines, i)
        '''print(i)
                for i in lines:
                    print(i)
        print('\n')'''

    if history[-1] in history[:-1]:
        if history.count(history[-1]) > 1:
            print(len(history), history.index(history[-1])+1)
            x =  1000000000 -len(history)
            y = (history.index(history[-1])+1)
            print(x,y,x%y)
            print((1000000000 -len(history)) % (len(history) - (history.index(history[-1])+1)))
            for i in range((1000000000 -len(history)) % (len(history) - (history.index(history[-1])+1))):
                #cancels out repeating cycles
                for i in dirs:
                    lines = slide(lines, i)
            break           
print(stresscalc(lines))