from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char_pairs = {i:j for i,j in zip(['2','3','4','5','6','7','8','9'], ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'])}

        results=[]
        for si in range(len(digits)):
            num = digits[si]
            chars = num_char_pairs[num]
            new_results=[]
            if len(results)==0:
                for c in chars:
                    new_results.append(c)
            else:
                for r in results:
                    for c in chars:
                        new_results.append(r+c)
            results=new_results
        return results

print(Solution().letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(Solution().letterCombinations("")) # []
print(Solution().letterCombinations("2")) # ["a","b","c"]
print(Solution().letterCombinations("987"))