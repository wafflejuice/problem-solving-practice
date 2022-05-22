import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
paper = []
for ni in range(n):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

tetromino_deltas = (
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    
    ((0, 0), (0, 1), (1, 0), (1, 1)),
    
    ((0, 0), (1, 0), (2, 0), (2, 1)),
    ((0, 1), (1, 1), (2, 0), (2, 1)),
    ((0, 2), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (0, 1), (1, 1), (2, 1)),
    ((0, 0), (0, 1), (1, 0), (2, 0)),
    ((0, 0), (0, 1), (0, 2), (1, 2)),
    ((0, 0), (0, 1), (0, 2), (1, 0)),
    
    ((0, 0), (1, 0), (1, 1), (2, 1)),
    ((0, 1), (1, 0), (1, 1), (2, 0)),
    ((0, 0), (0, 1), (1, 1), (1, 2)),
    ((0, 1), (0, 2), (1, 0), (1, 1)),
    
    ((0, 0), (0, 1), (0, 2), (1, 1)),
    ((0, 1), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (1, 1), (2, 0)),
    ((0, 1), (1, 0), (1, 1), (2, 1)),
)

max_sum = -1
for ni in range(n):
    for mi in range(m):
        for tetromino_delta in tetromino_deltas:
            tetromino_sum = 0
            for block_delta in tetromino_delta:
                y_pos = ni+block_delta[0]
                x_pos = mi+block_delta[1]
                if 0 <= y_pos < n and 0 <= x_pos < m:
                    tetromino_sum += paper[y_pos][x_pos]
                else:
                    break
            else:
                max_sum = max(max_sum, tetromino_sum)
print(max_sum)