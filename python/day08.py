from collections import defaultdict
with open('input') as f: lines = [x.strip('\n') for x in f]
Map = dict()
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = int(c)

max_x = len(lines[0])
max_y = len(lines)

def do_line_1(vis_set, points):
    height = -1
    for p in points:
        if Map[p] > height:
            vis_set.add(p)
            height = Map[p]

def do_line_2(score_dict, points):
    visible_by_next = [0] * 10
    for p in points:
        height = Map[p]
        score_dict[p] *= visible_by_next[height]
        for i in range(height+1):
            visible_by_next[i] = 1
        for i in range(height+1, 10):
            visible_by_next[i] += 1

def perform_part(doer_func, parm):
    for line in (((x,y) for y in range(max_y)) for x in range(max_x)):
        doer_func(parm, line)
    for line in (((x,y) for y in reversed(range(max_y))) for x in range(max_x)):
        doer_func(parm, line)
    for line in (((x,y) for x in range(max_x)) for y in range(max_y)):
        doer_func(parm, line)
    for line in (((x,y) for x in reversed(range(max_x))) for y in range(max_y)):
        doer_func(parm, line)

visible = set()
perform_part(do_line_1, visible)
print(len(visible))

scores = defaultdict(lambda:1)
perform_part(do_line_2, scores)
print(max(scores.values()))
