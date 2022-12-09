data = open('input').read().strip('\n')
def counted_groups(n):
    return enumerate(zip(*(data[i:] for i in range(n))), start=n)
def solutions(n):
    return filter(lambda x: len(set(x[1]))==n, counted_groups(n))
def solve(n):
    pos,_ = next(solutions(n))
    return pos
print(solve(4))
print(solve(14))
