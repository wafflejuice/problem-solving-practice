class Solution:
    def intToRoman(self, num: int) -> str:
        dividers=[1000,500,100,50,10,5,1]
        symbols=['M','D','C','L','X','V','I']
        roman=''
        for di in range(0, len(dividers), 2):
            div,num=divmod(num, dividers[di])
            if div>0:
                if div<4:
                    roman+=symbols[di]*div
                elif div==4:
                    roman += symbols[di]+symbols[di-1]
                elif div<9:
                    roman+=symbols[di-1]+symbols[di]*(div-5)
                elif div==9:
                    roman += symbols[di]+symbols[di-2]
                
        return roman
    
print(Solution().intToRoman(3))  # "III"
print(Solution().intToRoman(58)) # "LVIII"
print(Solution().intToRoman(1994)) # "MCMXCIV"