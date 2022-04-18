class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=1
        if (dividend>=0 and divisor<0) or (dividend<0 and divisor>0):
            sign=-1
        
        dividend,divisor=abs(dividend),abs(divisor)
        
        if dividend<divisor:
            return 0
        
        powers=[]
        two_powers=[]
        
        new_power=divisor
        new_two_power=1
        
        while new_power<=dividend:
            powers.append(new_power)
            two_powers.append(new_two_power)
            
            new_power += new_power
            new_two_power += new_two_power

        sum_=0
        for ri in range(len(powers)-1,-1,-1):
            while powers[ri]<=dividend:
                dividend -= powers[ri]
                sum_ += two_powers[ri]
                
        ans=sign * sum_
        ans=max(-2**31, min(ans, 2**31-1))
        
        return ans
        
print(Solution().divide(10, 3))  # 3
print(Solution().divide(7, -3)) # -2
print(Solution().divide(1, 1)) # 1
print(Solution().divide(-2147483648, -1)) # 2147483647