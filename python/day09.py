with open('input') as f: lines = [x.strip('\n') for x in f]
ssv = [x.split(' ') for x in lines]
def vec_add(p,q): return tuple(a+b for a,b in zip(p,q))
def vec_sub(p,q): return tuple(a-b for a,b in zip(p,q))
def tail_move(head, tail):
    x,y = vec_sub(head, tail)
    if x==0 and abs(y)==2:
        return (0, y//abs(y))
    if y==0 and abs(x)==2:
        return (x//abs(x), 0)
    if abs(x) == 2 or abs(y) == 2:
        return (x//abs(x), y//abs(y))
    return (0,0)

move = { 'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0) }
knots = [(0,0)] * 10
visited1 = set()
visited2 = set()

for line in ssv:
    for _ in range(int(line[1])):
        knots[0] = vec_add(knots[0], move[line[0]])
        for k in range(1, len(knots)):
            knots[k] = vec_add(knots[k], tail_move(knots[k-1], knots[k]))
        visited1.add(knots[1])
        visited2.add(knots[-1])
print(len(visited1))
print(len(visited2))
