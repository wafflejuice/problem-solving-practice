import math
from itertools import combinations

def solution(nums):
    odds, evens = [], []
    for n in nums:
        if n % 2 == 1: odds.append(n)
        else: evens.append(n)
    
    prime_candidates = list(map(sum, combinations(odds, 3)))
    for comb in combinations(evens, 2):
        for odd in odds:
            prime_candidates.append(sum(comb) + odd)
    
    prime_list = [i for i in range(3, 3001, 2)]
    for divider in range(3, int(math.sqrt(3001))+1, 2):
        for pi in range(len(prime_list)):
            if prime_list[pi] != divider and prime_list[pi] % divider == 0:
                prime_list[pi] = 0
    prime_list = list(filter(lambda x:x != 0, prime_list))
    
    cnt = 0
    for pc in prime_candidates:
        if pc in prime_list:
            cnt += 1
    
    return cnt

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))