from collections import deque

def solution(board, moves):
    height=len(board)
    width=len(board[0])
    queues=[deque() for _ in range(width)]
    for hi in range(height):
        for wi in range(width):
            if board[hi][wi] != 0:
                queues[wi].append(board[hi][wi])
    
    basket=deque()
    cnt=0
    for move in moves:
        if len(queues[move-1]) > 0:
            curr=queues[move-1].popleft()
            if len(basket) > 0:
                top=basket.pop()
                if top==curr:
                    cnt+=1
                else:
                    basket.append(top)
                    basket.append(curr)
            else:
                basket.append(curr)
    
    return cnt*2
 
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
print(solution(board, moves)) # 4