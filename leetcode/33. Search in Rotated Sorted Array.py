from typing import *
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sep=self.separate(nums)
        k=len(nums)-sep
        original_nums=nums[sep:]+nums[:sep]
        idx = bisect.bisect_left(original_nums, target)
        # print(f'sep={sep}, k={k}, idx={idx}, nums={nums}, original_nums={original_nums}, len(nums)-k+idx={len(nums)-k+idx}')
        if idx>=len(nums):
            return -1
        if original_nums[idx] == target:
            if idx<k:
                return len(nums)-k+idx
            else:
                return idx-k
        return -1

    def separate(self, nums):
        lo,hi=0,len(nums)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                return mid

            if nums[mid]<nums[hi]:
                hi=mid-1
            else:
                lo=mid+1
            # print(f'lo={lo}, hi={hi}')
        return lo

print(Solution().search(nums = [4,5,6,7,0,1,2], target = 0)) # 4
print(Solution().search(nums = [4,5,6,7,0,1,2], target = 3)) # -1
print(Solution().search(nums = [1], target = 0)) # -1

print(Solution().search(nums = [1], target = 2)) # -1
print(Solution().search(nums = [3,1], target = 3)) # 0
print(Solution().search(nums = [4,5,6,7,0,1,2], target = 5)) # 1
print(Solution().search(nums = [5,1,3], target = 1)) # 1
print(Solution().search(nums = [5,1,2,3,4], target = 1)) # 1


print(Solution().search(nums = [2,1], target = 1)) #
print(Solution().search(nums = [2,1], target = 2)) #