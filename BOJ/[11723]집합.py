import sys

m = int(sys.stdin.readline())
s = 0

for _ in range(m):
    input_ = sys.stdin.readline().rstrip().split()
    op, val = input_[0], None
    if len(input_) == 2:
        val = int(input_[1])

    if op == 'add':
        s |= 1 << val
    elif op == 'remove':
        s &= ~(1 << val)
    elif op == 'check':
        print((s >> val) & 1)
    elif op == 'toggle':
        s ^= 1 << val
    elif op == 'all':
        s = ~0
    elif op == 'empty':
        s = 0
