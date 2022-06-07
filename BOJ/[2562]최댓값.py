import sys

max_val = -1
max_idx = -1
for i in range(1, 10):
    val = int(sys.stdin.readline())
    if max_val < val:
        max_val = val
        max_idx = i

print(max_val)
print(max_idx)