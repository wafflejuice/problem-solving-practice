import math
from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix=""
        min_length=math.inf
        
        for s in strs:
            if len(s) < min_length:
                common_prefix=s
                min_length=len(s)
        
        for si in range(len(strs)):
            for ci in range(min(len(strs[si]), len(common_prefix))):
                if strs[si][ci] != common_prefix[ci]:
                    common_prefix=common_prefix[:ci]
                    break
        return common_prefix

print(Solution().longestCommonPrefix(["ab", "a"])) # a