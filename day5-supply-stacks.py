data0 = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3
 
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
import re

with open('day5-data.txt', 'r') as f:
    data1 = f.read()

def part1(x):
    initial_layout, instructions = re.sub('[^A-Z0-9_\n]', '',
                                          x.replace('    ', '_')).split('\n\n')
    start = initial_layout.split('\n')[::-1]
    stacks = [[] for _ in range(len(start))]
    for j in start:
        for i, q in enumerate(j):
            if q != '_':
                stacks[i].append(q)
    for l in instructions.split('\n')[:-1]:
        for *m, n, o in l.split()[::-1]:
            for p in range(int("".join(m))):
                stacks[int(o)-1].append(stacks[int(n)-1].pop())
    return "".join(i[-1] for i in stacks)

print(part1(data1))
