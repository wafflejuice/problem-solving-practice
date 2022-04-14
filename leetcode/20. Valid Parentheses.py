from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                
                top=stack.pop()
                if top=='(' and char==')':
                    continue
                elif top=='{' and char=='}':
                    continue
                elif top=='[' and char==']':
                    continue
                 
                return False
            
        return len(stack)==0

print(Solution().isValid("()")) # true
print(Solution().isValid("()[]{}")) # true
print(Solution().isValid("(]")) # false
print(Solution().isValid("[")) # false # I missed not closed case.

print(Solution().isValid("([)]")) # false
