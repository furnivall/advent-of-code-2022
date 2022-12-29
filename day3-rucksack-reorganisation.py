def part1():
    with open('day3-clue.txt', 'r') as f:
        return sum(map(lambda x: ord(x) - 96 if x.islower() else ord(x) - 38, ["".join(set(i[0:int(len(i) / 2)]).intersection(i[int(len(i) / 2) : len(i)])) for i in f.read().splitlines()]))

def part2():
    with open('day3-clue.txt', 'r') as f:
            data = f.read().splitlines()
            return sum([ord(y) -96 if y.islower() else ord(y) - 38 for y in [x for x in str([set.intersection(*map(set, j)) for j in [data[i:i+3] for i in range(0, len(data), 3)]]) if x.isalpha()]])


print(part1())
print(part2())
