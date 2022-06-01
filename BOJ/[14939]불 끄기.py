import copy
import sys

matrix = []
for _ in range(10):
    matrix.append(list(map(lambda x:1 if x == 'O' else 0, list(sys.stdin.readline().rstrip()))))

def flip(matrix, y, x):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if abs(dy) + abs(dx) <= 1:
                if 0 <= y + dy < 10 and 0 <= x + dx < 10:
                    matrix[y + dy][x + dx] = 1 - matrix[y + dy][x + dx]

min_cnt = 100
is_possible = False
for bit in range(1024):
    matrix_copy = copy.deepcopy(matrix)
    cnt = 0
    for xi in range(10):
        if bit & 1 == 1:
            flip(matrix_copy, 0, xi)
            cnt += 1
        bit //= 2
    
    for yi in range(1, 10):
        for xi in range(10):
            if matrix_copy[yi-1][xi] == 1:
                flip(matrix_copy, yi, xi)
                cnt += 1
    
    is_complete = True
    for yi in range(10):
        for xi in range(10):
            if matrix_copy[yi][xi] == 1:
                is_complete = False
                break
    
    if is_complete:
        is_possible = True
        min_cnt = min(min_cnt, cnt)

if is_possible:
    print(min_cnt)
else:
    print(-1)