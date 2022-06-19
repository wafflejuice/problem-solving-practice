import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    priorities = list(map(int, sys.stdin.readline().rstrip().split()))
    
    cnt = 0
    while True:
        val = priorities.pop(0)
        is_turn = True
        for priority in priorities:
            if priority > val:
                is_turn = False
                break

        if is_turn:
            cnt += 1
            if m == 0:
                print(cnt)
                break
        else:
            priorities.append(val)
            
        m = (m - 1) % len(priorities)