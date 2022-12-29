def part1():
    with open("day2-1-input.txt") as f:
        # map to subtract 64 from ascii vals to get actual scores for each of our moves. 
        data = map(lambda i: (ord(i[0])-64, ord(i[2])-87), f.readlines())
        return sum([(3 if (y - x) == 0 else 0 if (y - x) in (-1, 2) else 6) + y for x, y in data])

def part2():
    with open("day2-1-input.txt") as f:
        # reduced value by 1 for opponent's ascii so as to utilise zero indexing
        data = list(map(lambda i: (ord(i[0])-65, ord(i[2])-87), f.readlines()))
        return sum([x + 4 if y == 2 else [3,1,2][x] if y == 1 else [8, 9, 7][x] for x, y in data])


print(part1())
print(part2())
