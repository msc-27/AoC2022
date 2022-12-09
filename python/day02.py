with open('input') as f: lines = [x.strip('\n') for x in f]
ssv = [x.split(' ') for x in lines]

choice_score = {'R':1, 'P':2, 'S':3}
result_score = {'R': {'R':3, 'P':6, 'S':0}, \
                'P': {'R':0, 'P':3, 'S':6}, \
                'S': {'R':6, 'P':0, 'S':3} }
elf_map = {'A':'R', 'B':'P', 'C':'S'}
you_map = {'X':'R', 'Y':'P', 'Z':'S'}
want_map = {'X':0, 'Y':3, 'Z':6}

score = 0
for elf_raw, you_raw in ssv:
    elf = elf_map[elf_raw]
    you = you_map[you_raw]
    score += choice_score[you] + result_score[elf][you]
print(score)

score = 0
for elf_raw, want_raw in ssv:
    elf = elf_map[elf_raw]
    want = want_map[want_raw]
    you = next(x for x in result_score[elf] if result_score[elf][x] == want)
    score += choice_score[you] + result_score[elf][you]
print(score)
