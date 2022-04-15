from typing import *
from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses_combinations=[]
        # BFS
        queue=deque()
        queue.append(('(',n-1,n))
        while len(queue)>0:
            string=queue.popleft()
            
            if string[1]==0 and string[2]==0:
                parentheses_combinations.append(string[0])
                continue

            if string[1] > 0:
                queue.append((string[0]+'(', string[1]-1, string[2]))
            if string[1]<string[2]:
                queue.append((string[0]+')',string[1],string[2]-1))
                
        return parentheses_combinations

print(Solution().generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(Solution().generateParenthesis(1)) # ["()"]