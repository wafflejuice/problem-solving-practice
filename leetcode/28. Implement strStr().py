class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        
        for hi in range(len(haystack)):
            is_found=True
            for ni in range(len(needle)):
                if hi+ni<len(haystack):
                    if haystack[hi+ni]==needle[ni]:
                        pass
                    elif haystack[hi+ni]!=needle[ni]:
                        is_found=False
                        break
                else:
                    if ni<len(needle):
                        is_found=False
                        break
            if is_found:
                return hi
        return -1

print(Solution().strStr("hello", "ll")) # 2
print(Solution().strStr("aaaaa", "bba")) # -1
print(Solution().strStr("", "")) # 0
print(Solution().strStr("", "hi")) # -1