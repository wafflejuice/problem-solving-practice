import sys

n, s = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

i, j = 0, 0
sub_sum = 0
min_cnt = 100001

while True:
    if sub_sum < s:
        if j == n:
            break
        sub_sum += arr[j]
        j += 1
    else:
        if j - i < min_cnt:
            min_cnt = j - i

        sub_sum -= arr[i]
        i += 1

if min_cnt == 100001:
    print(0)
else:
    print(min_cnt)