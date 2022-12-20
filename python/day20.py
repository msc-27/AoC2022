with open('input') as f: lines = [x.strip('\n') for x in f]
values = [(n,int(v)) for n,v in enumerate(lines)]

def mix(values, orig_values, key=1):
    length = len(values)
    key %= (length - 1)
    for v in orig_values:
        index = values.index(v)
        values.pop(index)
        index = (index + v[1] * key) % (length - 1)
        values[index:] = [v] + values[index:]

def decrypt(values, key=1, rounds=1):
    length = len(values)
    mixed_values = values.copy()
    for i in range(rounds): mix(mixed_values, values, key)
    v = next(v for v in mixed_values if v[1] == 0)
    index = mixed_values.index(v)
    return key * sum(mixed_values[(index+x) % length][1] for x in [1000,2000,3000])

print(decrypt(values))
print(decrypt(values, 811589153, 10))
