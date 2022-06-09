import sys

word = sys.stdin.readline().rstrip()
cnts = [0 for _ in range(26)]
for ch in word.lower():
    cnts[ord(ch)-ord('a')] += 1
max_cnt = max(cnts)
if cnts.count(max_cnt) >= 2:
    print('?')
else:
    print(chr(ord('a')+cnts.index(max_cnt)).upper())