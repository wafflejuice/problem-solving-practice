import sys

k, n = map(int, sys.stdin.readline().rstrip().split())
lengs = [int(sys.stdin.readline()) for _ in range(k)]

i, j = 1, max(lengs)
max_div = -1
while i<=j:
    mid = i+(j-i)//2

    cnt = 0
    for leng in lengs:
        cnt += leng // mid
    if cnt >= n:
        max_div = max(max_div, mid)
        i = mid+1
    else:
        j = mid-1

print(max_div)
