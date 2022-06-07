import sys

n = int(sys.stdin.readline())
max_val = -1000001
min_val = 1000001
nums = list(map(int, sys.stdin.readline().rstrip().split()))
for num in nums:
    max_val = max(max_val, num)
    min_val = min(min_val, num)
print(min_val, max_val)