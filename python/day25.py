with open('input') as f: lines = [x.strip('\n') for x in f]
symbol = { -2:'=', -1:'-', 0:'0', 1:'1', 2:'2' }

total = 0
for line in lines:
    b = 1
    for c in reversed(line):
        if c == '2': total += b*2
        if c == '1': total += b
        if c == '-': total -= b
        if c == '=': total -= b*2
        b *= 5
b = 1
while True:
    if b * 2.5 > total: break
    b *= 5
digits = []
while b:
    digit = -2
    test = -b * 1.5
    while total > test:
        digit += 1
        test += b
    digits.append(symbol[digit])
    total -= digit * b 
    b //= 5
print(''.join(digits))
