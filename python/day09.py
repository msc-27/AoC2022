from collections import defaultdict
with open('input') as f: lines = [x.strip('\n') for x in f]
ssv = [x.split(' ') for x in lines]
def vec_add(p,q): return tuple(a+b for a,b in zip(p,q))
def vec_sub(p,q): return tuple(a-b for a,b in zip(p,q))

knots = [(0,0)] * 10
visited1 = set()
visited2 = set()

move = { 'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0) }

shift = defaultdict(lambda:(0,0), \
       { (2,0):(1,0), (0,2):(0,1), (-2,0):(-1,0), (0,-2):(0,-1), \
         (2,1):(1,1), (2,-1):(1,-1), (-2,1):(-1,1), (-2,-1):(-1,-1), \
         (1,2):(1,1), (1,-2):(1,-1), (-1,2):(-1,1), (-1,-2):(-1,-1), \
         (2,2):(1,1), (-2,-2):(-1,-1), (2,-2):(1,-1), (-2,2):(-1,1) } )

for line in ssv:
    for _ in range(int(line[1])):
        knots[0] = vec_add(knots[0], move[line[0]])
        for k in range(1, len(knots)):
            diff = vec_sub(knots[k-1], knots[k])
            knots[k] = vec_add(knots[k], shift[diff])
        visited1.add(knots[1])
        visited2.add(knots[-1])
print(len(visited1))
print(len(visited2))
