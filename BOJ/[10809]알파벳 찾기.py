import sys

s = sys.stdin.readline().rstrip()
encounter = [-1 for _ in range(26)]
for i, ch in enumerate(s):
    idx = ord(ch) - ord('a')
    if encounter[idx] == -1:
        encounter[idx] = i
print(' '.join(list(map(str, encounter))))