tiles=[[i2 for i2 in i.strip()] for i in open('10data.txt', 'r').readlines()]
z = '1234567890'
z = [i for i in z]
#1,2,3
#4, ,6
#7,8,9
#pipetype:position of entry, position of exit(interchangeable)
pipes = {'|':[[0,1], [0, -1]],
'-':[[-1,0], [1, 0]],
'L':[[0,1], [1,0]],
'J':[[-1,0], [0,1]],
'7':[[0,-1], [-1,0]],
'F':[[0,-1], [1,0]],}
cont = 1
for row in range(len(tiles)):
    if cont:
        for col in range(len(tiles)):
            if tiles[row][col] == 'S':
                pos = row, col
                cont = 0
print(pos)

def adj(pos):
    x,y = pos
    adjacent = []
    for ymod in range(-1,2):
        for xmod in range(-1,2):
            try:adjacent.append((tiles[y+ymod][x + xmod], [x + xmod], [y+ymod]))
            except:adjacent.append(('.', x + xmod, y+ymod))
    return adjacent
#needs some mechanism to stop backtracking, store previous location
steps = 0
cont = 1
while cont:
    movebreak = 0 
    adjacent = adj(pos)
    print('new char', pos, tiles[pos[0]][pos[1]])
    for i in adjacent:
        if i[0] == 'S' and steps > 2: cont = 0;steps+= 1
        if not movebreak:
            if i[0] in pipes:
                print(i[0])
                
                #if x + predicted offset = actual pos, and y, set new pos
                for switcher in range(2):
                    print('expected x', pos[0]+pipes[i[0]][switcher][0])
                    print('actual x', i[1][0])
                    print('expected y', pos[1]+pipes[i[0]][switcher][1])
                    print('actual y', i[2][0])
                    if (pos[0]+pipes[i[0]][switcher][0] == i[1][0] and pos[1]+pipes[i[0]][switcher][1] == i[2][0]):
                        print('moving')
                        movebreak = 1
                        pos = i[1][0], i[2][0]
                        steps += 1
                
