import sys

def is_vps(str):
    stack = 0
    for ch in str:
        if ch == '(':
            stack += 1
        else:
            if stack > 0:
                stack -= 1
            else:
                return False
    
    if stack > 0:
        return False
    return True

t = int(sys.stdin.readline())
for _ in range(t):
    str = sys.stdin.readline().rstrip()
    if is_vps(str):
        print('YES')
    else:
        print('NO')