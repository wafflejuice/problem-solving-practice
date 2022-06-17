import heapq
import sys

n = int(sys.stdin.readline())
l = []
for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    heapq.heappush(l, (age, i, name))

for i in range(n):
    age, _, name = heapq.heappop(l)
    print(str(age) + ' ' + name)