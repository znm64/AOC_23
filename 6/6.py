#part 1
lines = [i.strip() for i in open('6data.txt', 'r').readlines()]
times = lines[0][13:].split('     ')
dist = lines[1][12:].split('   ')
times = [int(i) for i in times]
dist = [int(i) for i in dist]
freq = [0 for i in range(len(times))]
for num, i in enumerate(times):
    for time in range(i):
        if (time*(i-time))>dist[num]:
            freq[num] += 1
            print(time, ' ', num)
a = 1
for i in freq:
    a *= i
print(a)

#part 2
import operator
lines = [i.strip() for i in open('6data.txt', 'r').readlines()]
times = lines[0][13:].replace('     ', '')
dist = lines[1][12:].replace('   ', '')
times = [int(times)]
dist = [int(dist)]
freq = [0 for i in range(len(times))]
for num, i in enumerate(times):
    for time in range(i):
        if (time*(i-time))>dist[num]:
            freq[num] += 1

print(freq)