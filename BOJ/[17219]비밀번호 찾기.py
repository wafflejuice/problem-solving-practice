import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
site_pw_pairs = dict()
for _ in range(n):
    site, pw = sys.stdin.readline().rstrip().split()
    site_pw_pairs[site] = pw
for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(site_pw_pairs[site])