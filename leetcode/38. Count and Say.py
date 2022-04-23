class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        digits = self.countAndSay(n - 1)
        
        say = ""
        cnt = 0
        for i in range(len(digits)+1):
            if i==0:
                cnt=1
            elif i==len(digits):
                say += str(cnt)
                say += digits[i - 1]
            else:
                if digits[i-1] != digits[i]:
                    say += str(cnt)
                    say += digits[i-1]
                    cnt = 1
                else:
                    cnt += 1
        
        return say
    
print(Solution().countAndSay(n = 1)) # "1"
print(Solution().countAndSay(n = 4)) # "1211"