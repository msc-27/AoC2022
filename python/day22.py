from collections import defaultdict
import moves
with open('input') as f:
    paras = [p.split('\n') for p in f.read().strip('\n').split('\n\n')]

Map = defaultdict(lambda:' ')
for y,line in enumerate(paras[0]):
    for x,c in enumerate(line):
        Map[(x,y)] = c

def step_map(t):
    t.move()
    if Map[t.loc] == ' ':
        x,y = t.loc
        if t.facing == moves.Dir.N:
            t.loc = max((X,Y) for X,Y in Map if X==x and Map[(X,Y)] != ' ')
        if t.facing == moves.Dir.S:
            t.loc = min((X,Y) for X,Y in Map if X==x and Map[(X,Y)] != ' ')
        if t.facing == moves.Dir.W:
            t.loc = max((X,Y) for X,Y in Map if Y==y and Map[(X,Y)] != ' ')
        if t.facing == moves.Dir.E:
            t.loc = min((X,Y) for X,Y in Map if Y==y and Map[(X,Y)] != ' ')
    if Map[t.loc] == '#':
        t.turnV()
        step_map(t)
        t.turnV()

def step_cube(t):
# Programmed only for this cube layout:
#  BA
#  C
# ED
# F
    t.move()
    x,y = t.loc
    f = t.facing
    if x == 150: # A > to D <
        t.loc = (99, 100+(49-y))
        t.facing = moves.Dir.W
    if y == -1 and x >= 100: # A ^ to F ^
        t.loc = (x-100, 199)
    if y == -1 and x < 100: # B ^ to F >
        t.loc = (0, 150+(x-50))
        t.facing = moves.Dir.E
    if x >= 100 and y == 50 and f == moves.Dir.S: # A v to C <
        t.loc = (99, 50+(x-100))
        t.facing = moves.Dir.W
    if x == 49 and y <= 49: # B < to E >
        t.loc = (0, 100+(49-y))
        t.facing = moves.Dir.E
    if x == 49 and 50 <= y < 100 and f == moves.Dir.W: # C < to E v
        t.loc = (y-50, 100)
        t.facing = moves.Dir.S
    if x == 100 and 50 <= y < 100 and f == moves.Dir.E: # C > to A ^
        t.loc = (100+(y-50), 49)
        t.facing = moves.Dir.N
    if x == 100 and y >= 100: # D > to A <
        t.loc = (149, 149-y)
        t.facing = moves.Dir.W
    if y == 150 and x >= 50 and f == moves.Dir.S: # D v to F <
        t.loc = (49, 150+(x-50)) 
        t.facing = moves.Dir.W
    if x < 50 and y == 99 and f == moves.Dir.N: # E ^ to C >
        t.loc = (50, 50+x)
        t.facing = moves.Dir.E
    if x == -1 and y < 150: # E < to B >
        t.loc = (50, 149-y) 
        t.facing = moves.Dir.E
    if x == -1 and y >= 150: # F < to B v
        t.loc = (50+(y-150), 0)
        t.facing = moves.Dir.S
    if x == 50 and y >= 150 and f == moves.Dir.E: # F > to D ^
        t.loc = (50+(y-150), 149)
        t.facing = moves.Dir.N
    if y == 200: # F v to A v
        t.loc = (100+x, 0)
        
    if Map[(t.loc)] == '#':
        t.turnV()
        step_cube(t)
        t.turnV()

def instructions(s):
    val = 0
    for i in range(len(s)):
        if s[i].isdigit():
            val *= 10
            val += int(s[i])
        else:
            yield val
            val = 0
            yield s[i]
    if val != 0: yield val

def solve(step_func):
    init_loc = min((X,Y) for X,Y in Map if Y==0 and Map[(X,Y)] != ' ')
    turt = moves.Turtle(init_loc, moves.Dir.E)
    for inst in instructions(paras[1][0]):
        if type(inst) == int:
            for i in range(inst): step_func(turt)
        else:
            if inst == 'R':
                turt.turnR()
            else:
                turt.turnL()
    decode = {moves.Dir.E: 0, moves.Dir.S: 1, moves.Dir.W: 2, moves.Dir.N: 3}
    return 1000*(turt.loc[1]+1) + 4*(turt.loc[0]+1) + decode[turt.facing]

print(solve(step_map))
print(solve(step_cube))
