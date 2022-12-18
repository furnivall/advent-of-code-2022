def part1():
    with open ('day1-1-input.txt') as f: elves = f.read().split('\n\n')
    print(max([sum(map(int,elf.split('\n'))) for elf in elves[:-1]]))

def part2():
    with open ('day1-1-input.txt') as f: elves = f.read().split('\n\n')
    print(sum(sorted([sum(map(int, elf.split('\n'))) for elf in elves[:-1]], reverse=True)[0:3]))

print("Part 1 answer: "), part1()
print("Part 2 answer: "), part2()
