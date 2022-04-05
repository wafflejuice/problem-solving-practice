class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        ans=''
        
        len_ = len(s)
        zig_size = (numRows-1)*2 if numRows > 1 else 1 # corner case: numRows=1
        
        row=0
        while row < numRows:
            zig=0
            while zig*zig_size+row < len_:
                ans += s[zig*zig_size+row]
                
                if row != 0 and row != numRows-1:
                    if (zig+1)*zig_size-row < len_:
                        ans += s[(zig+1)*zig_size-row]
                zig+=1
            row+=1
        
        return ans

print(Solution().convert("PAYPALISHIRING", 3))
print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("A", 1))