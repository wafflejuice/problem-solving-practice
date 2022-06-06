import sys

n = int(sys.stdin.readline())
ps = list(map(int, sys.stdin.readline().rstrip().split()))

ps.sort()
sum_ = 0
for i in range(n):
    sum_ += ps[i] * (n-i)
print(sum_)