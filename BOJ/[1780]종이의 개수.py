import sys

n = int(sys.stdin.readline())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    
counts = [0, 0, 0]

def validate(n, row, col):
    num = matrix[row][col]

    if n == 1:
        counts[num+1] += 1
        return
    
    for ri in range(row, row+n):
        for ci in range(col, col+n):
            if num != matrix[ri][ci]:
                n //= 3
                validate(n, row, col)
                validate(n, row, col+n)
                validate(n, row, col+n+n)
                validate(n, row+n, col)
                validate(n, row+n, col+n)
                validate(n, row+n, col+n+n)
                validate(n, row+n+n, col)
                validate(n, row+n+n, col+n)
                validate(n, row+n+n, col+n+n)
                
                break
        else:
            continue
            
        break
    else:
        counts[num+1] += 1
    
validate(n, 0, 0)

print(counts[0])
print(counts[1])
print(counts[2])