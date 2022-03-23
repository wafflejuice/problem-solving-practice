def solution(m, n, board):
    board = board_format(m, n, board)

    answer = 0
    while True:
        cnt, board = remove(m, n, board)
        # print(board)
        if cnt == 0:
            break
        answer += cnt

    return answer

def board_format(m, n, board):
    new_board = []
    for yi in range(m):
        new_board.append([])
        for xi in range(n):
            new_board[yi].append(board[yi][xi])
    return new_board

def remove(m, n, board):
    board_checker = []
    for yi in range(m):
        board_checker.append([])
        for xi in range(n):
                board_checker[yi].append(0)

    for yi in range(m-1):
        for xi in range(n-1):
            if quad(board, yi, xi):
                board_checker[yi][xi] = 1
                board_checker[yi+1][xi] = 1
                board_checker[yi][xi+1] = 1
                board_checker[yi+1][xi+1] = 1

    cnt = 0
    for yi in range(m):
        for xi in range(n):
            if board_checker[yi][xi] == 1:
                cnt += 1

    board = x_board(m, n, board, board_checker)
    updated_board = update_board(m, n, board)

    return cnt, updated_board

def x_board(m, n, board, board_checker):
    for yi in range(m):
        for xi in range(n):
            if board_checker[yi][xi] == 1:
                board[yi][xi] = "X"
    return board

def update_board(m, n, board):
    for yi in range(m-1, 0, -1):
        for xi in range(n):
            for rri in range(yi):
                if board[yi][xi] == "X":
                    # print(f'yi={yi}, xi={xi}')
                    # print_board(m, n, board)

                    for ri in range(yi, 0, -1):
                        board[ri][xi] = board[ri - 1][xi]
                        board[ri - 1][xi] = "X"

                    # board[yi][xi] = board[yi - 1][xi]
                    # board[yi-1][xi] = "X"

    return board

def print_board(m, n, board):
    for yi in range(m):
        a=''
        for xi in range(n):
            a+=board[yi][xi]
        print(a)
    print()

def quad(board, y, x):
    if board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1] != "X":
        return True
    return False

def dup(y1, x1, y2, x2):
    if y1 == y2 and x1 == x2:
        return 4
    if y1 == y2 and abs(x1-x2)==1:
        return 2
    if abs(y1-y2)==1 and x1==x2:
        return 2
    if abs(y1-y2)==1 and abs(x1-x2)==1:
        return 1
    return 0

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

# 약 1시간...