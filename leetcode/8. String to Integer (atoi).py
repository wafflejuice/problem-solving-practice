class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ABS_INT_MAX = str(pow(2, 31)-1)
        ABS_INT_MIN = str(pow(2, 31))
        
        s=s.lstrip(' ')
        
        is_neg=False
        if len(s)>0:
            if s[0] =='+':
                s=s[1:]
            elif s[0]=='-':
                is_neg=True
                s=s[1:]
        
        s=s.lstrip('0')
        
        i=0
        while i<len(s):
            if s[i] not in list('1234567890'):
                s=s[:i]
                break
            i+=1
        
        if len(s) == 0:
            return 0

        ans=s
        
        if not is_neg:
            if len(s)>len(ABS_INT_MAX) or (len(s)==len(ABS_INT_MAX) and ABS_INT_MAX < s):
                ans=ABS_INT_MAX
        if is_neg:
            if len(s)>len(ABS_INT_MAX) or (len(s)==len(ABS_INT_MIN) and ABS_INT_MIN < s):
                ans=ABS_INT_MIN
        
        ans=int(ans)
        ans=ans*(-1) if is_neg else ans
        
        return ans

print(Solution().myAtoi("42")) # 42
print(Solution().myAtoi("   -42")) # -42
print(Solution().myAtoi("4193 with words")) # 4193
print(Solution().myAtoi("words and 987")) #
print(Solution().myAtoi("-91283472332")) # -2147483648
print(Solution().myAtoi("  0000000000012345678")) # 12345678
