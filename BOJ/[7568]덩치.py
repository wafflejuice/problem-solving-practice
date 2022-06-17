import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().rstrip().split())))
rankings = []
for i in range(n):
    ranking = 1
    for j in range(n):
        if i == j:
            continue
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            ranking += 1
    rankings.append(ranking)
print(' '.join(map(str, rankings)))