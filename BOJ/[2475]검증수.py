import sys

nums = map(int, sys.stdin.readline().rstrip().split())
sum_ = 0
for num in nums:
    sum_ += num * num
print(sum_ % 10)