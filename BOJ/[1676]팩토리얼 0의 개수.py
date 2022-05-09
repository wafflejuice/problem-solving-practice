import sys

n = int(sys.stdin.readline())

two_cnt = 0
five_cnt = 0
for i in range(2, n+1):
    while i % 2 == 0:
        two_cnt += 1
        i = i // 2
    while i % 5 == 0:
        five_cnt += 1
        i = i // 5

print(min(two_cnt, five_cnt))