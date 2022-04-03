class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_=0
        i,j=0,0
        while i<len(s) and j<len(s):
            k=i
            while k<j:
                if s[k]==s[j]:
                    break
                k+=1
            if k==j:
                max_ = max(max_,j-i+1)
                j+=1
            else:
                i=k+1
        return max_

print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
print(Solution().lengthOfLongestSubstring("bbbbb"))  # 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
print(Solution().lengthOfLongestSubstring(" ")) # 1
print(Solution().lengthOfLongestSubstring("dvdf")) # 3

# two pointer with skipping