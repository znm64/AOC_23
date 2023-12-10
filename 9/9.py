lines = open('9data.txt', 'r').readlines()
lines = [i.strip().split(' ') for i in lines]
nums = []
for i in lines:
    current = []
    for i2 in i:
        current.append(int(i2))
    nums.append(current)
originallengths = [len(i) for i in nums]
for count, i in enumerate(nums):
    x = [i]
    y = []
    while False in [i == 0 for i in x[-1]]:
        for count2, num in enumerate(x[-1][:-1]):
            y.append(x[-1][count2+1] - num)
        x.append(y)
        y = []
    nums[count]+=(x[1:])

for count, i in enumerate(nums):
    nums[count] = [nums[count][:originallengths[count]]]+ nums[count][originallengths[count]:]
    print(nums[count])

for prog_num, progression in enumerate(nums):
    nums[prog_num].reverse()
    for diff_num, differences in enumerate(nums[prog_num]):
        print(differences, diff_num)
        if diff_num == 0:
            nums[prog_num][0].append(0)
        else:
            nums[prog_num][diff_num].append(nums[prog_num][diff_num][-1] + nums[prog_num][diff_num-1][-1])
            nums[prog_num][diff_num].insert(0, nums[prog_num][diff_num][0] - nums[prog_num][diff_num-1][0])

print('\nfinal\n')
for i in nums:
    print(i)

sum = 0
for i in nums:
    sum += i[-1][-1]
print(sum)

sum = 0
for i in nums:
    sum += i[-1][0]
print(sum)