with open('input') as f: lines = [x.strip('\n') for x in f]
ssv = [x.split(' ') for x in lines]

grid = [['.']*40 for i in range(6)]
signal = 0; cycle = 0; reg = 1; X,Y = 0,0

def tick():
    global grid, signal, cycle, reg, X, Y
    cycle += 1
    if cycle in (20,60,100,140,180,220):
        signal += cycle * reg
    if X in (reg-1, reg, reg+1): grid[Y][X] = '#'
    X += 1
    if X == 40:
        Y += 1
        X = 0

for line in ssv:
    if line[0] == 'noop':
        tick()
    else:
        tick()
        tick()
        reg += int(line[1])

print(signal)
for x in grid: print(''.join(x))
