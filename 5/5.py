#part 1
raw = [i for i in open('5data.txt', 'r').readlines()]
raw.insert(1, raw[0][7:])
processed = []
current = []
for i in raw:
    if not ':' in i:
        current.append(i)
    else:
        processed.append(current)
        current = []
processed.append(current)
processed_2 = []
for count, i in enumerate(processed):
    current = []
    for count2, i2, in enumerate(i):
        i2 = i2.strip()
        current.append(i2.split(' '))
    processed_2.append(current[:-1])
    
seeds = processed_2[1]
mappings = processed_2[2:]
newseeds = []
seeds = [int(i) for i in seeds[0]]
mappings = [[[int(i) for i in j] for j in k] for k in mappings]
x = [[0 for i in range(20)] for i in range(8)]
#for each seed
for count, seed in enumerate(seeds):
    #for each mapping type
    for mapnum, fullmap in enumerate(mappings):
        changemade = False
        #for each individual map triplet
        for i in fullmap:
            if i[1] <= seed and seed <= i[1]+i[2]+1 and not changemade:
                seed = seed - i[1]+i[0]
                changemade = True
    seeds[count] = seed

print(min(seeds))