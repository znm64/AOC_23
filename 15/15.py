'''x = open('15data.txt', 'r').read().strip().split(',')
currentvalues = [0 for i in range(len(x))]
def hash(string, count):
    for i in string:
        currentvalues[count] = (17*(currentvalues[count]+ord(i)))%256
    return currentvalues

for count, i in enumerate(x):
    currentvalues = hash(i, count)
'''
#part 2
x = open('15data.txt', 'r').read().strip().split(',')
currentvalues = [0 for i in range(len(x))]

def hash(string):
    result = 0
    for i in string:
        result = (17*(result+ord(i)))%256
    return result

boxes = [[] for i in range(256)]

for step in x:
    label = (''.join([i if i.isalpha() else '' for i in step]))
    labhash = hash(label)
    print(label)
    if '=' in step:
        toreplace = -1
        for i in boxes[labhash]:
            if label in i:
                toreplace = i
        if toreplace != -1: 
            boxes[labhash] = [step if i == toreplace else i for i in boxes[labhash]]
        else:
            boxes[labhash].append(step)
    elif '-' in step:
        toremove = -1
        for i in boxes[labhash]:
            if label in i:
                toremove = i
        if toremove != -1: 
            boxes[labhash].remove(toremove)
            print('removed', toremove)
final = 0
print(boxes)
for count, box in enumerate(boxes):
    for position, lens in enumerate(box):
        print(lens,(count+1), (position+1), int(''.join([i if i.isnumeric() else '' for i in lens])))
        final += ((count+1)*(position+1)*int(''.join([i if i.isnumeric() else '' for i in lens])))
print(final)