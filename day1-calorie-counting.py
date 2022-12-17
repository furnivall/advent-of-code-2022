with open ('day1-1-input.txt') as f:
    elves = f.read().split('\n\n')
print(max([sum(map(int,elf.split('\n'))) for elf in elves[:-1]]))


