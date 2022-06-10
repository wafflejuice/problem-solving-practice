import math
import sys

nums = []
for _ in range(3):
    nums.append(int(sys.stdin.readline()))
nums = math.prod(nums)

cnts = [0 for _ in range(10)]
while nums > 0:
    cnts[nums % 10] += 1
    nums //= 10

for i in range(10):
    print(cnts[i])