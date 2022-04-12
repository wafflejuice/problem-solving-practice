class Solution:
    def romanToInt(self, s: str) -> int:
        sum_ = 0
        ti=0
        while ti<len(s):
            if s[ti] == 'I':
                if ti+1<len(s) and s[ti+1] == 'V':
                    sum_ += 4
                    ti+=2
                    continue
                elif ti+1<len(s) and s[ti+1] == 'X':
                    sum_ += 9
                    ti+=2
                    continue
                sum_ += 1
            elif s[ti] == 'V':
                sum_ += 5
            elif s[ti] == 'X':
                if ti+1<len(s) and s[ti+1] == 'L':
                    sum_ += 40
                    ti+=2
                    continue
                elif ti+1<len(s) and s[ti+1] == 'C':
                    sum_ += 90
                    ti+=2
                    continue
                sum_ += 10
            elif s[ti] == 'L':
                sum_ += 50
            elif s[ti] == 'C':
                if ti+1<len(s) and s[ti+1] == 'D':
                    sum_ += 400
                    ti+=2
                    continue
                elif ti+1<len(s) and s[ti+1] == 'M':
                    sum_ += 900
                    ti+=2
                    continue
                sum_ += 100
            elif s[ti] == 'D':
                sum_ += 500
            elif s[ti] == 'M':
                sum_ += 1000
                
            ti+=1
            
        return sum_
        
print(Solution().romanToInt("III")) # 3
print(Solution().romanToInt("LVIII")) # 58
print(Solution().romanToInt("MCMXCIV")) # 1994