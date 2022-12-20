import itertools
from collections import defaultdict
data = open('input').read().strip('\n')
movements = itertools.cycle(data)

shapes = [ [0b00111100,   \
            0b00000000,   \
            0b00000000,   \
            0b00000000 ], \
                          \
           [0b00010000,   \
            0b00111000,   \
            0b00010000,   \
            0b00000000 ], \
                          \
           [0b00111000,   \
            0b00001000,   \
            0b00001000,   \
            0b00000000 ], \
                          \
           [0b00100000,   \
            0b00100000,   \
            0b00100000,   \
            0b00100000 ], \
                          \
           [0b00110000,   \
            0b00110000,   \
            0b00000000,   \
            0b00000000 ]  \
         ]
shape_sequence = itertools.cycle(shapes)

lines = defaultdict(lambda:0b100000001)
lines[0] = 0b111111111

def move_shape(shape, baseline, movement):
    global lines
    if movement == '<':
        new_shape = [x << 1 for x in shape]
    else:
        new_shape = [x >> 1 for x in shape]
    if all( (new_shape[i] & lines[baseline+i] == 0 for i in range(4)) ):
        shape[:] = new_shape

def drop_shape(shape, baseline):
    global lines
    if all( (shape[i] & lines[baseline+i-1] == 0 for i in range(4)) ):
        return baseline - 1, False
    else:
        return baseline, True

stack_height = 0
baseline = 4
shape = next(shape_sequence).copy()
rocks = 0

while True:
    movement = next(movements)
    move_shape(shape, baseline, movement)
    baseline, stopped = drop_shape(shape, baseline)
    if stopped:
        for i in range(4): lines[baseline+i] |= shape[i]
        stack_height = max(h for h in range(stack_height, stack_height+5) if lines[h] != 0b100000001)
        rocks += 1
        if rocks == 2022:
            print(stack_height)
            break
        shape = next(shape_sequence).copy()
        baseline = stack_height + 4
