#part2
#just overwrote the code for part 1
debugreg = []
lines = open('data.txt', 'r').readlines()
line_nums = [[] for i in range(len(lines))]
#originally, the mappin of words to num was one:1, but for part 2, i changed the mapping  to also include the first and last letters
#note that twone should evaluate to 21, not 2ne, in part 2. This was not mentioned in the instuctions, and does not affect the test case
#this wouln't make a difference if you were only searching for the values, but i chose to replace the values and then read for digits(not the best way to do it) 
map = [['o1e', "one"], ['t2o', "two"], ['t3e', "three"], ['f4r', "four"], ['f5e', "five"], ['s6x', "six"], ['s7n', "seven"], ['e8t', "eight"], ['n9e', "nine"]]
for linenum, i in enumerate(lines):
    temp = ''
    for char in i:
        temp += char
        for element in map:
            temp = temp.replace(element[1], str(element[0]))
    print(temp)
    for char in (temp.strip()):
        if char.isnumeric():
            line_nums[linenum].append(int(char))

total = 0
for i in line_nums:
    total+=(int(str(i[0])+str(i[-1])))
    debugreg.append(int(str(i[0])+str(i[-1])))
print(total)
