import sys

l = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

r = 31
m = 1234567891
hash = 0
for i, ch in enumerate(s):
    hash += (ord(ch)-ord('a')+1)*(r**i) % m
print(hash % m)