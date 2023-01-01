with open('day4-data.txt', 'r') as f:
    data = f.read().splitlines()

def part1(data):
    return len([(q, r) for q, r in [(set(range(int(l[0]),int(l[1])+1)), set(range(int(m[0]), int(m[1])+1))) for l, m in [(j.split('-'), k.split('-')) for j, k in [i.split(',') for i in data]]] if r.issubset(q) or q.issubset(r)])

def part2(data):
    return len([(q, r) for q, r in ([(set(range(int(l[0]),int(l[1])+1)), set(range(int(m[0]), int(m[1])+1))) for l, m in [(j.split('-'), k.split('-')) for j, k in [i.split(',') for i in data]]]) if len(q.intersection(r)) > 0])


print(part1(data))
print(part2(data))
