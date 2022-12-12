with open('input') as f: lines = [x.strip('\n') for x in f]
ssv = [x.split(' ') for x in lines]

root = ('/',)
dirs = {root:[[],0]} # [children, total size]

for line in ssv:
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                path = root
            elif line[2] == '..':
                path = path[:-1]
            else:
                path = path + (line[2],)
    elif line[0] == 'dir':
        dirs[path][0].append(line[1])
        dirs[path + tuple([line[1]])] = [[],0]
    else:
        for i in range(0,len(path)):
            dirs[path[:i+1]][1] += int(line[0])

print(sum(s[1] for s in dirs.values() if s[1] <= 100000))

unused = 70000000 - dirs[root][1]
req = 30000000 - unused
print(min(s[1] for s in dirs.values() if s[1] >= req))
