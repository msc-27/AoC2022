from collections import defaultdict
import astar
import neigh
from math import gcd
def manhat(p,q): return sum(abs(a-b) for a,b in zip(p,q))
with open('input') as f: lines = [x.strip('\n') for x in f]

Map = defaultdict(lambda:'#')
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = c

out = 0
width = len(lines[0])-2
height = len(lines)-2
cycle = width * height // gcd(width, height)

up = set(p for p in Map if Map[p] == '^')
down = set(p for p in Map if Map[p] == 'v')
left = set(p for p in Map if Map[p] == '<')
right = set(p for p in Map if Map[p] == '>')

def blizzard(p, t): # Is there a blizzard at p at time t?
    x,y = p
    y_up    = ((y + t - 1) % height) + 1
    y_down  = ((y - t - 1) % height) + 1
    x_left  = ((x + t - 1) % width) + 1
    x_right = ((x - t - 1) % width) + 1
    return (x,y_up) in up or \
           (x,y_down) in down or \
           (x_left,y) in left or \
           (x_right,y) in right

def trans(s): # (position, minute % cycle)
    p, t = s
    for q in neigh.atmanhat(p,1):
        if not blizzard(q, t+1) and Map[q] != '#':
            yield ((q, (t+1) % cycle), 1)
    if not blizzard(p, t+1):
        yield ((p, (t+1) % cycle), 1)

start = (1,0)
end = (width, height+1)

def start_f(s): return s[0] == start
def end_f(s): return s[0] == end

def start_est(s): return manhat(s[0], start)
def end_est(s): return manhat(s[0], end)

a = astar.astar((start, 0), trans, end_f, end_est)
steps = a.run()[0]
print(steps)

a = astar.astar((end, steps % cycle), trans, start_f, start_est)
steps += a.run()[0]
a = astar.astar(((1,0), steps % cycle), trans, end_f, end_est)
steps += a.run()[0]
print(steps)
