from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        initial_length=len(nums)
        duplicate_num=0
        ni=0
        while ni<initial_length-1-duplicate_num:
            if nums[ni]==nums[ni+1]:
                nums.pop(ni+1)
                duplicate_num+=1
            else:
                ni+=1
        
        return initial_length-duplicate_num

nums1=[1,1,2]
print(Solution().removeDuplicates(nums1))  # 2, [1,2,_]
print(nums1)

nums2=[0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums2)) # 5, [0,1,2,3,4,_,_,_,_,_]
print(nums2)