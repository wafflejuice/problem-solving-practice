from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.next_board(board)
    
    def valid_range(self, m, n, y, x):
        return 0<=y<m and 0<=x<n
    
    def live_neighbors(self, board, y, x):
        m=len(board)
        n=len(board[0])
        
        cnt=0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy==0 and dx==0:
                    continue
                if self.valid_range(m, n, y+dy, x+dx):
                    cnt+=board[y+dy][x+dx]
        return cnt
        
    def next_state(self, board, y, x):
        live_neighbors_cnt = self.live_neighbors(board, y, x)
        if board[y][x] == 1:
            if live_neighbors_cnt < 2:
                return 0
            elif live_neighbors_cnt < 4:
                return 1
            else:
                return 0
        else:
            if live_neighbors_cnt == 3:
                return 1
            else:
                return 0
    
    def next_board(self, board):
        m=len(board)
        n=len(board[0])
        new_board = [[0 for x in range(n)] for x in range(m)]
        
        for yi in range(m):
            for xi in range(n):
                new_board[yi][xi] = self.next_state(board, yi, xi)
        
        for yi in range(m):
            board[yi]=new_board[yi]
            
def print_board(board):
    m=len(board)
    
    for yi in range(m):
        print(board[yi])

boards=[
    [[0,1,0],[0,0,1],[1,1,1],[0,0,0]], # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    [[1,1],[1,0]] # [[1,1],[1,1]]
]

for board in boards:
    print('####################')
    print('initial board...')
    print_board(board)
    Solution().gameOfLife(board)
    print('altered board...')
    print_board(board)
    print('####################')
