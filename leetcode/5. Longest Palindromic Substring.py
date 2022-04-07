class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        cl,cr=0,0 # candidate palindrome's left & right indices
        m=0 # middle of odd-size palindrome
        while m<len(s):
            d=0
            while m-d >= 0 and m+d<len(s):
                if s[m-d] != s[m+d]:
                    break
                d+=1
            if 1+(d-1)*2 > cr-cl+1:
                cl=m-(d-1)
                cr=m+(d-1)
            m+=1

        ml=0 # middle-left of even-size palindrome
        while ml+1<len(s):
            d=0
            while ml-d >= 0 and ml+1+d < len(s):
                if s[ml-d] != s[ml+1+d]:
                    break
                d+=1
            if 2+(d-1)*2 > cr-cl+1:
                cl=ml-(d-1)
                cr=ml+1+(d-1)
            ml+=1
        return s[cl:cr+1]

print(Solution().longestPalindrome("babad")) # bab
print(Solution().longestPalindrome("cbbd")) # bb
