import sys

t = int(sys.stdin.readline())
for _ in range(t):
    r, s = sys.stdin.readline().rstrip().split()
    r = int(r)
    print(''.join(map(lambda x:x*r, s)))