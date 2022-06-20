import sys

n = int(sys.stdin.readline())
occurrences = [False for _ in range(2000001)]
for _ in range(n):
    occurrences[int(sys.stdin.readline()) + 1000000] = True
for i, occurrence in enumerate(occurrences):
    if occurrence:
        print(i - 1000000)