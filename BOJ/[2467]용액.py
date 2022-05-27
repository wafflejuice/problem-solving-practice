import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

i, j = 0, n-1
min_abs_sum = 2000000001
alkali_candidate, acid_candidate = None, None

while i < j:
    sum_ = arr[i]+arr[j]

    if abs(sum_) < min_abs_sum:
        min_abs_sum = abs(sum_)
        alkali_candidate, acid_candidate = arr[i], arr[j]

    if sum_ < 0:
        i += 1
    else:
        j -= 1

print(alkali_candidate, acid_candidate)