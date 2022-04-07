class Solution(object):
    def isMatchSimple(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        import re
        pp = re.compile("^"+p+"$")
        return pp.match(s) is not None

print(Solution().isMatch("aa", "a")) # false
print(Solution().isMatch("aa", "a*")) # true
print(Solution().isMatch("ab", ".*")) # true