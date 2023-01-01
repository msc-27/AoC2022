import re
with open('input') as f: lines = [x.strip('\n') for x in f]
numbers = [list(map(int, re.findall('-?[0-9]+',line))) for line in lines]
def manhat(p,q): return sum(abs(a-b) for a,b in zip(p,q))

part1_y = 2000000
part2_limits = [0, 4000000]

def disjoint(a, b): # are ranges a and b disjoint?
    a1,a2 = a
    b1,b2 = b
    if b2 < a1 or b1 > a2: return True
    return False

def unite(a, b): # return union of two overlapping ranges
    a1,a2 = a
    b1,b2 = b
    return [min(a1,b1), max(a2,b2)]

def overlap_size(a, b): # return size of overlap of two ranges
    a1,a2 = a
    b1,b2 = b
    return min(a2,b2) - max(a1,b1) + 1

def evaluate_sensors(data, test_y):
    sensors = []
    beacons_on_test_row = set()
    for line in numbers:
        sx, sy, bx, by = line
        r = manhat((sx,sy), (bx,by))
        sensors.append((sx, sy, r))
        if by == test_y: beacons_on_test_row.add(bx)
    sensors.sort(key = lambda s: s[1]) # sort in Y-order
    return sensors, len(beacons_on_test_row)

def test_line(test_y, limits=None):
    shrinking_overlap = None
    covers = [] # list of disjoint ranges covered by sensors
    for x, y, r in sensors:
        if y-r <= test_y <= y+r:
            dist = abs(test_y - y)
            spread = r - dist
            if limits:
                cover = [max(limits[0],x-spread), min(limits[1],x+spread)]
            else:
                cover = [x-spread, x+spread]
            covers_new = []
            for interval in covers:
                if disjoint(cover, interval):
                    covers_new.append(interval)
                else:
                    if y <= test_y:
                        overlap = overlap_size(cover, interval)
                        if not shrinking_overlap:
                            shrinking_overlap = overlap
                        else:
                            shrinking_overlap = min(shrinking_overlap, overlap)
                    cover = unite(cover, interval)
            covers_new.append(cover)
            covers = covers_new
    return covers, shrinking_overlap

sensors, n_beacons = evaluate_sensors(numbers, part1_y)
covers, _ = test_line(part1_y)
print(sum(x2-x1+1 for x1,x2 in covers) - n_beacons)

# Start at line 0.
# At each line, test whether the entire search range is covered by sensors.
# If not, then skip ahead to either:
# a. the first line on which the smallest overlap between two sensors whose
#    ranges are shrinking will disappear; or, if no such overlap exists,
# b. the next line on which a sensor can be found 
#    (all current overlaps must be growing or static until we get there)
test = 0
while True:
    covers, overlap = test_line(test, part2_limits)
    if len(covers) > 1: break
    if overlap:
        test += (overlap + 1) // 2
    else:
        test = min(y for x,y,r in sensors if y > test)
covers.sort()
print((covers[0][1]+1) * 4000000 + test)
