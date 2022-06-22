import sys

t = int(sys.stdin.readline())
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    y = n % h
    x = n // h
    if y == 0:
        y = h
    else:
        x += 1
        
    if x < 10:
        print(str(y) + '0' + str(x))
    else:
        print(str(y) + str(x))