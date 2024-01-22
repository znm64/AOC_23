commands = [[i.split(' ')[0], int(i.split(' ')[1]), i.split(' ')[2]] for i in open('17data.txt', 'r').read().split('\n')]
maxes = [0]*4
#height up, height down, width right, width left
for i in commands:
    print(i)
    if i[0] == 'D': maxes[1] += i[1]
    if i[0] == 'R': maxes[2] += i[1]
    if i[0] == 'U': maxes[0] += i[1]
    if i[0] == 'L': maxes[3] += i[1]
print(maxes)
matrix = [[0]*(maxes[0]+maxes[1])]*(maxes[2]+maxes[3])
matrix[0][1] = "test"
print(matrix)
currentpos = [maxes[3],maxes[0]]
currentpos = [0,0]
for i in commands:
    if i[0] == 'R' or i[0] == 'L':
        modifier = (1 if i[0]=='R' else -1)
        for i in range(i[1]):
            currentpos[0]+=1*modifier
            matrix[1][0] = 1
            print(currentpos)
    else:
        modifier = (1 if i[0]=='U' else -1)
        for i in range(i[1]):
            currentpos[1]+=1*modifier
            matrix[currentpos[1]][currentpos[0]] = 1
            print(currentpos)
for i in matrix: print(i)