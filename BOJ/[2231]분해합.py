import sys

n = int(sys.stdin.readline())

for num in range(1, n):
    sum_ = num
    for ch in str(num):
        sum_ += int(ch)
    if sum_ == n:
        print(num)
        break
else:
    print(0)