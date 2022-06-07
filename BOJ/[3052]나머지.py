import sys

s = set()
for _ in range(10):
    s.add(int(sys.stdin.readline()) % 42)
print(len(s))