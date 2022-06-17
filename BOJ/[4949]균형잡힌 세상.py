import sys
from collections import deque

def is_balanced(line):
    q = deque()

    for ch in line:
        if ch == '(':
            q.append(ch)
        elif ch == '[':
            q.append(ch)
        elif ch == ')':
            if len(q) == 0:
                return False
            if q.pop() != '(':
                return False
        elif ch == ']':
            if len(q) == 0:
                return False
            if q.pop() != '[':
                return False
    if len(q) > 0:
        return False

    return True


while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break

    if is_balanced(line):
        print('yes')
    else:
        print('no')