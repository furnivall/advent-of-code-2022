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
#     print(data)
def part1(x):
    initial_layout, instructions = re.sub('[^A-Z0-9_\n]', '',
                                          x.replace('   ', '_')).split('\n\n')
    start = initial_layout.split('\n')[:-1][::-1]
    print(start)
    stacks = [[] for i in range(len(start))]
    for j in start:
        for i, q in enumerate(j):
            if q != '_':
                stacks[i].append(q)
    print(stacks)
    for l in instructions.split('\n'):
        for m, n, o in l.split()[::-1]:
            print(m, n, o)
            for p in range(int(m)):
                stacks[int(o)-1].append(stacks[int(n)-1].pop())
    print(stacks)
    return "".join(i[-1] for i in stacks)


# print(initial_state[0].split('\n')[:-1])
# y = initial_state[0].split('\n')[:-1]
# print(y)
# initial_state =  re.sub('[''^A-Za-z0-9_\n]','', x[:x.rfind(']')].replace('    ','_'))
# instructions = re.sub(, '', x[x.find('move'):])
# print(instructions)


print(part1(data0))
