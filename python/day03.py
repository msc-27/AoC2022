with open('input') as f: lines = [x.strip('\n') for x in f]
def convert(c):
    if c <= 'Z':
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1

part1 = 0
for line in lines:
    size = len(line)
    s1 = set(line[:size//2])
    s2 = set(line[size//2:])
    common = s1 & s2
    for c in common: part1 += convert(c)
print(part1)

part2 = 0
for a,b,c in zip(lines[0::3], lines[1::3], lines[2::3]):
    common = set(a) & set(b) & set(c)
    for c in common: part2 += convert(c)
print(part2)
