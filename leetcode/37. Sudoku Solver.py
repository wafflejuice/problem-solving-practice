from functools import reduce
from typing import *

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        digits = '123456789'
        available_digits_at_row = [set(digits) for _ in range(9)]
        available_digits_at_col = [set(digits) for _ in range(9)]
        available_digits_at_grid = [set(digits) for _ in range(9)]

        undefined = []
        for yi, row in enumerate(board):
            for xi, digit in enumerate(row):
                if digit == '.':
                    undefined.append((yi, xi))
                else:
                    available_digits_at_row[yi].remove(digit)
                    available_digits_at_col[xi].remove(digit)
                    available_digits_at_grid[yi//3*3+xi//3].remove(digit)
                    
        self.dfs(board, 0, undefined, available_digits_at_row, available_digits_at_col, available_digits_at_grid)
        
    def dfs(self, board, idx, undefined, available_digits_at_row, available_digits_at_col, available_digits_at_grid):
        if idx == len(undefined):
            return True

        y, x = undefined[idx]
        sets = [available_digits_at_row[y], available_digits_at_col[x], available_digits_at_grid[y//3*3+x//3]]
        choices = reduce(set.intersection, sets)
        
        for chosen in choices:
            board[y][x] = chosen
            for s in sets:
                s.remove(chosen)
            
            if self.dfs(board, idx+1, undefined, available_digits_at_row, available_digits_at_col, available_digits_at_grid):
                return True
            
            board[y][x] = '.'
            for s in sets:
                s.add(chosen)
        
def print_board(board):
    for yi in range(9):
        print(board[yi])
    print()

def print_both(board, candidates):
    for yi in range(9):
        for xi in range(9):
            if board[yi][xi] == '.':
                print(candidates[yi][xi], end=' ')
            else:
                print(board[yi][xi], end=' ')
        print()
    print()


input_board1=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
input_board2=[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
input_board3=[[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
input_board4=[["1",".",".",".","7",".",".","3","."],["8","3",".","6",".",".",".",".","."],[".",".","2","9",".",".","6",".","8"],["6",".",".",".",".","4","9",".","7"],[".","9",".",".",".",".",".","5","."],["3",".","7","5",".",".",".",".","4"],["2",".","3",".",".","9","1",".","."],[".",".",".",".",".","2",".","4","3"],[".","4",".",".","8",".",".",".","9"]]
input_board5=[[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]

input_boards=[input_board1, input_board2, input_board3, input_board4, input_board5]
for input_board in input_boards:
    print_board(input_board)
    Solution().solveSudoku(input_board)
    print_board(input_board)