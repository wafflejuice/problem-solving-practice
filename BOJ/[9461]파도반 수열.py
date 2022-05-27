import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [-1] * 90
    curr = 10
    while curr < n:
        curr += 1
        p[curr] = p[curr-1] + p[curr-5]

    print(p[n])