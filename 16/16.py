#backslashes are read into the matrix as doubles, due to character escapes
#there is a workaround, but its simple to just read each double backspace as a single, later on 
matrix = [[i2 for i2 in i.strip()] for i in open('16data.txt', 'r').readlines()]
parallel = [[[0, 0] for i2 in i] for i in matrix]
#beams is an array of all the current beams. 
# each element stores x, y, direction
beams = [[0,0,1]]
while len(beams)!=0:
    for count, i in enumerate(beams):
        calc = 1
        x,y,dir = i[0], i[1], i[2]
        if dir == 0 or dir == 2:
            y+=(dir-1)
        else:
            #dir = 1 or 3
            x+=-(dir-2)
        try:
            location = matrix[y][x]
            print(location)
            beams[count] = [x, y, dir]
            if parallel[y][x] == [1, dir] or x<0 or y<0: 
                beams.pop(count)
                calc = 0
            parallel[y][x] = 1, dir
        except:
            beams.pop(count)
            calc = 0
            #it has gone out of range of the matrix, so is deleted
        if calc:
            current = matrix[y][x]
            if current == '.':
                pass
                #added so that i can test to make sure every beam encounters one of the conditions
            elif current == '/':
                if dir == 0:
                    dir = 1
                elif dir == 1:
                    dir = 0
                elif dir == 3:
                    dir = 2
                elif dir == 2:
                    dir = 3
            elif current == '\\':
                if dir == 0:
                    dir = 3
                elif dir == 3:
                    dir = 0
                elif dir == 2:
                    dir = 1
                elif dir == 1:
                    dir = 2
            elif current == '-':
                if dir == 0 or dir == 2:
                    beams+=[x,y,1], [x, y, 3]
                    beams.pop(count)
                    calc = 0
            elif current == '|':
                if dir == 1 or dir == 3:
                    beams+= [x,y,2], [x, y, 0]
                    beams.pop(count)
                    calc = 0
            if calc:
                beams[count][2] = dir
    print(beams)
total = 0
for i in parallel:
    total += i.count(1)
print(total)