#part1
lines = [i.strip() for i in open('3data.txt', 'r').readlines()]
raw = ''
#got the symbol list by removing any digits or periods from the raw text, copying the
#terminal result back into the code.
symbols = ['*', '/', '+', '%', '&', '-', '=', '$', '@', '#']
#lol didnt need this function in the end - some people used a solution with this?
#the idea here was to find symbols first, then to find the numbers afterwards.
#that would be a lot longer - about 100 lines, and annoying to code, since searching for 
#an adjacent number is fiddly.
def findnum(x, y):
    first, last = x, x
    front, back = True, True
    while front or back:
        if lines[y][first-1].isdigit() == True:
            first -= 1
        else:
            front = False
        if lines[y][last+1].isdigit() == True:
            last += 1
        else:
            back = False
    print(lines[y][first])
    print(lines[y][last])
    return lines[y][first:last+1], first, last 
#finds all the numbers in the data, saves them to array nums.
#each element of nums is a list, first element is the number, second and third are the 
#line positions(x then y).
def searchnums():
    nums = []
    for step, i in enumerate(lines):
        refreshed = True
        current = ''
        currentstart = 0
        for count, char in enumerate(i):
            if char.isdigit():
                if current == '':
                    currentstart = count
                current += char
                if count +1 >= len(i):
                    refreshed = True
                else:
                    refreshed = (i[count+1] == '.' or i[count+1] in symbols)
                if refreshed:
                    nums.append([current, currentstart, step])
                    current = ''
    return nums
#searches all adjacent characters around the number for symbols. valid is a flag, starts
#as false, only gets set to true if a symbol is found. 
#needed to account for the search staying within the limits of the 2d array, thus the if...if 
#monstrosity(could have been done better).
x = (searchnums())
print(x)
total = 0
for i in x:
    valid = False
    y = i[2]
    x = i[1]
    testtrigger = (True if i[0] == '896' else False)
    for charnum in range(len(i[0])):
        for a in range(-1+charnum, 2+charnum):
            for b in range(-1, 2):
                modifierx = a
                modifiery = b
                if x + a == -1:
                    a += 1
                if x+a == -2:
                    a += 2
                if x + a == 140:
                    a -= 1
                if x + a == 141:
                    a -= 2
                if y + b == -1:
                    b += 1
                if y+b == -2:
                    b += 2
                if y + b == 140:
                    b -= 1
                if y + b == 141:
                    b -= 2
                if lines[y+b][x+a] in symbols:
                    valid = True   
                    
    if valid == True:
        total += int(i[0])
        print(int(i[0]))
print(total)

#part 2
lines = [i.strip() for i in open('data.txt', 'r').readlines()]
raw = ''
symbolmap = [[[] for i in range(len(lines[0]))] for i in range(len(lines)+1)]
#symbols was changed here, since it was easier than changing the code later.
#allsymbols replaced its original use.
symbols = ['*']
allsymbols = ['*', '/', '+', '%', '&', '-', '=', '$', '@', '#']
def searchnums():
    nums = []
    for step, i in enumerate(lines):
        refreshed = True
        current = ''
        currentstart = 0
        for count, char in enumerate(i):
            if char.isdigit():
                if current == '':
                    currentstart = count
                current += char
                if count +1 >= len(i):
                    refreshed = True
                else:
                    refreshed = (i[count+1] == '.' or i[count+1] in allsymbols)
                if refreshed:
                    nums.append([current, currentstart, step])
                    current = ''
    return nums
x = (searchnums())
total = 0
#saves numbers to the asterisk adjacent to them, if one is found.
#if theres only two numbers to each asterisk, their product is added to the final sum.
for i in x:
    valid = False
    y = i[2]
    x = i[1]
    symbollocation = 0,0
    testtrigger = (True if i[0] == '0' else False)
    for charnum in range(len(i[0])):
        for a in range(-1+charnum, 2+charnum):
            for b in range(-1, 2):
                modifierx = a
                modifiery = b
                if x + a == -1:
                    a += 1
                if x+a == -2:
                    a += 2
                if x + a == len(lines[0]):
                    a -= 1
                if x + a == (len(lines[0])+1):
                    a -= 2
                if y + b == -1:
                    b += 1
                if y+b == -2:
                    b += 2
                if y + b == len(lines):
                    b -= 1
                if y + b == (len(lines)+1):
                    b -= 2
                if lines[y+b][x+a] in symbols:
                    valid = True   
                    locationsymbol = [y+b, x+a]
    if valid == True:
        symbolmap[locationsymbol[0]][locationsymbol[1]].append(i[0])
total = 0
for i in symbolmap:
    for i2 in i:
        if len(i2) == 2:
            total += int(i2[0])*int(i2[1])
print(total)