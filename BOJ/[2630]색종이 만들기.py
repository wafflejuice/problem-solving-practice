import sys

n = int(sys.stdin.readline())
matrix = []

for ri in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

def check(rs, cs, size):
    flag = matrix[rs][cs]
    for dr in range(size):
        for dc in range(size):
            if matrix[rs+dr][cs+dc] != flag:
                return False
    return True

def s(rs, cs, size):
    if check(rs, cs, size):
        return (0, 1) if matrix[rs][cs] == 1 else (1, 0)
    
    size = size//2
    paper_cnts = [s(rs, cs, size), s(rs, cs + size, size), s(rs + size, cs, size), s(rs + size, cs + size, size)]
    white_cnt, blue_cnt = zip(*paper_cnts)
    
    return sum(white_cnt), sum(blue_cnt)

res = s(0, 0, n)
print(res[0])
print(res[1])