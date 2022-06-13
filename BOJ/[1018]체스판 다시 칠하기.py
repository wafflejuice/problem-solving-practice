import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    board.append(sys.stdin.readline().rstrip())
    
def check(sr, sc):
    min_cnt = 64
    for color in ['B', 'W']:
        cnt = 0
        for ri in range(8):
            for ci in range(8):
                if (ri + ci) % 2 == 0:
                    if board[sr + ri][sc + ci] != color:
                        cnt += 1
                else:
                    if board[sr + ri][sc + ci] == color:
                        cnt += 1
        min_cnt = min(min_cnt, cnt)
    return min_cnt

min_cnt = 64
for ri in range(n-8+1):
    for ci in range(m-8+1):
        min_cnt = min(min_cnt, check(ri, ci))

print(min_cnt)