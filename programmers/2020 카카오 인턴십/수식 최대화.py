import re
from itertools import permutations
from functools import reduce

def solution(expression):
    nums = list(map(int, re.split('[+\-*]', expression)))
    ops = list(filter(lambda x:x in ['+', '-', '*'], expression))
    expression = list(reduce(lambda x, y: x+y, zip(nums, ops))) + [nums[-1]]
    
    op_types = set(ops)
    permutations_ = permutations(op_types, len(op_types))
    
    results=[]
    for permutation in permutations_:
        expression_copy = expression.copy()
        for op in permutation:
            i=1
            while i < len(expression_copy):
                if op == expression_copy[i]:
                    if op == '-':
                        new_element = expression_copy[i-1] - expression_copy[i+1]
                    elif op == '*':
                        new_element = expression_copy[i-1] * expression_copy[i+1]
                    else:
                        new_element = expression_copy[i-1] + expression_copy[i+1]
                    expression_copy = expression_copy[:i-1] + [new_element] + expression_copy[i+1+1:]
                else:
                    i += 2
        results.append(expression_copy[0])
        
    return max(list(map(abs, results)))

print(solution("100-200*300-500+20")) # 60420
print(solution("50*6-3*2")) # 300