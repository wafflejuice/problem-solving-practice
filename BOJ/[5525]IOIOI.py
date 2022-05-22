import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

centers = ['I', 'O']

candidates = []
toggle = 0
begin = 0
is_begun = False
for i in range(m):
    if is_begun:
        if s[i] == centers[toggle]:
            toggle = 1 - toggle
        else:
            if s[i] == 'I':
                candidates.append((begin, i))
                is_begun = True
                begin = i
            else:
                candidates.append((begin, i-1))
                is_begun = False
    else:
        if s[i] == 'I':
            begin = i
            toggle = 1
            is_begun = True
            
if is_begun:
    candidates.append((begin, m))

cnt = 0
for candidate in candidates:
    d = candidate[1] - candidate[0]
    if d < 2*n + 1:
        continue
    else:
        cnt += (d - (2*n+1)) // 2 + 1

print(cnt)