import math
from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # length == 1
        if len(nums) == 1:
            return
        
        # go to lowest possible order
        is_reverse = True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                is_reverse = False
                break
        
        if is_reverse:
            for i in range(len(nums)-1):
                for j in range(len(nums)-1-i):
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
            return
        
        #
        if nums[-2] < nums[-1]:
            nums[-2],nums[-1]=nums[-1],nums[-2]
            return
        
        border=-1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                border=i-1
                break
                
        max_min_idx=-1
        max_min=math.inf
        for i in range(border+1, len(nums)):
            if nums[border]<nums[i]<max_min:
                max_min_idx=i
        nums[border],nums[max_min_idx]=nums[max_min_idx],nums[border]
        
        for i in range(len(nums) - border):
            for j in range(border+1, len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

input_nums = [[1,2,3], [3,2,1], [1,1,5],
              [2,2,3,4,2,3], [3,1,2,6,5,4,2,2,1]]
for nums in input_nums:
    print(f'from\t{nums}')
    Solution().nextPermutation(nums)
    print(f'to\t\t{nums}')
    print()
    
# [1,3,2]
# [1,2,3]
# [1,5,1]