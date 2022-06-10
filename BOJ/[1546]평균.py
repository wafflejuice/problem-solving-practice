import sys

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().rstrip().split()))
max_score = max(scores)
scores = list(map(lambda x:x/max_score*100, scores))
print(sum(scores)/n)