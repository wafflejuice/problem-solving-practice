import sys

n = int(sys.stdin.readline())

cnt = 0
for five_bag_cnt in range(n // 5, -1, -1):
    cnt = five_bag_cnt
    remains = n - 5 * five_bag_cnt
    if remains % 3 == 0:
        cnt += remains // 3
        print(cnt)
        break
else:
    print(-1)