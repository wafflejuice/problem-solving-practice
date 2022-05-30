import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

names = ['']
name_idx_pair = dict()
for i in range(n):
    name = sys.stdin.readline().rstrip()
    names.append(name)
    name_idx_pair[name] = i+1
for _ in range(m):
    target = sys.stdin.readline().rstrip()
    if target.isdigit():
        print(names[int(target)])
    else:
        print(name_idx_pair[target])