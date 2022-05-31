import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().rstrip().split()))

subsum_cnt_dict_a = dict()
subsum_cnt_dict_b = dict()

def construct_subsum_cnt_dict(leng, arr, subsum_cnt):
    for i in range(leng):
        subsum = 0
        for j in range(i, leng):
            subsum += arr[j]
            if subsum not in subsum_cnt:
                subsum_cnt[subsum] = 0
            subsum_cnt[subsum] += 1

construct_subsum_cnt_dict(n, a, subsum_cnt_dict_a)
construct_subsum_cnt_dict(m, b, subsum_cnt_dict_b)

cnt = 0
for subsum_a in subsum_cnt_dict_a:
    target_subsum_b = t - subsum_a
    if target_subsum_b in subsum_cnt_dict_b:
        cnt += subsum_cnt_dict_a[subsum_a] * subsum_cnt_dict_b[target_subsum_b]

print(cnt)