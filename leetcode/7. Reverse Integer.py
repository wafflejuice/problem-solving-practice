class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        is_neg=True if x<0 else False
        x=x*(-1) if is_neg else x
        ps=str(x)
        rps=''.join(reversed(ps))

        # -2147483648 ~ 2147483647
        if len(rps) == 10 and rps[0] != '0':
            if not is_neg and rps > '2147483647':
                return 0
            elif is_neg and rps > '2147483648':
                return 0

        x=int(rps)
        x=x*(-1) if is_neg else x

        return x

print(Solution().reverse(123)) # 321
print(Solution().reverse(-123)) # -321
print(Solution().reverse(120)) # 21
print(Solution().reverse(-2147483412)) # -2143847412