import sys

n = int(sys.stdin.readline())
nums = []
cnts = [0 for _ in range(8001)]
for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
    cnts[num+4000] += 1
nums.sort()

print(round(sum(nums) / n))
print(nums[n//2])

candies = []
max_cnt = max(cnts)
for i in range(len(cnts)):
    if cnts[i] == max_cnt:
        candies.append(i-4000)
if len(candies) == 1:
    print(candies[0])
else:
    print(candies[1])

print(nums[-1] - nums[0])