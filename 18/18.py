instructions = [[i2 for i2 in i.strip().split(' ')] for i in open('18data.txt', 'r').readlines()]
depth = sum([int(i[1]) if i[0] == 'D' else 0 for i in instructions])+1
width = sum([int(i[1]) if i[0] == 'R' else 0 for i in instructions])+1
matrix = [['.' for i in range(width)] for i in range(depth)]
curpos = [0,0]
for i in instructions:
    previous = curpos.copy()
    dir,dist = i[0],i[1]
    if dir == 'R' or dir == 'L':
        dir = (1 if dir=='R' else -1)    
        curpos[0] += (int(dist)*dir)

    else:
        dir = (1 if dir=='D' else -1)    
        curpos[1] += (int(dist)*dir)

    if i[0] == 'R' or i[0] == 'L':
        if dir == 1:
            matrix[curpos[1]][previous[0]:curpos[0]] = '#'*(abs(curpos[0]-previous[0]))
        else:   
            matrix[curpos[1]][curpos[0]+1:previous[0]+1] = '#'*(abs(curpos[0]-previous[0]))
    else:
        if dir == 1:
            for i2 in range(previous[1], curpos[1]):
                matrix[i2][curpos[0]] = '#'
        else:
            for i2 in range(previous[1], curpos[1], -1):
                matrix[i2][curpos[0]] = '#'
for y,row in enumerate(matrix):
    pos = []
    for index, i in enumerate(row):
        if i == '#': pos.append(index)
    if len(pos) != len(matrix[0]) and len(pos)!= 0:
       print(pos)
       matrix[y][pos[0]:pos[-1]] = '#'*(pos[-1]-pos[0])
final = 0
for i in matrix:
    final += i.count('#')
print(final)