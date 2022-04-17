from typing import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        initial_len=len(nums)
        remove_num=0
        ni=0
        while ni<initial_len-remove_num:
            if nums[ni]==val:
                nums.pop(ni)
                remove_num+=1
            else:
                ni+=1
        return initial_len-remove_num

        # less-efficient in time & space both.
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)

nums1=[3,2,2,3]
print(Solution().removeElement(nums1, 3))  # 2, [2,2,_,_]
print(nums1)

nums2=[0,1,2,2,3,0,4,2]
print(Solution().removeElement(nums2, 2)) # 5, [0,1,4,0,3,_,_,_]
print(nums2)