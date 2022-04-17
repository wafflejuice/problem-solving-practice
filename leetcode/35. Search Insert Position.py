from typing import *
import bisect

class Solution:
    # using lib.
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
    """
    
    # implement myself
    """
    def searchInsert(self, nums, target):
        lo,hi=0,len(nums)
        prelo,prehi=lo,hi

        while lo<hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                prelo=lo
                lo=mid+1
            else:
                prehi=hi
                hi=mid

        for i in range(prelo, prehi):
            if target<=nums[i]:
                return i

        return prehi
    """
    
    # reference discussion
    # https://leetcode.com/problems/search-insert-position/discuss/15101/C++-O(logn)-Binary-Search-that-handles-duplicate
    def searchInsert(self, nums, target):
        lo, hi = 0, len(nums)-1
    
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1

        # (1) At this point, low > high. That is, low >= high+1
        # (2) From the invariant, we know that the index is between [low, high+1], so low <= high+1. Follwing from (1), now we know low == high+1.
        # (3) Following from (2), the index is between [low, high+1] = [low, low], which means that low is the desired index
        # Therefore, we return low as the answer. You can also return high+1 as the result, since low == high+1
        return lo
    
print(Solution().searchInsert([1,3,5,6], 5)) # 2
print(Solution().searchInsert([1,3,5,6], 2)) # 1
print(Solution().searchInsert([1,3,5,6], 7)) # 4
print(Solution().searchInsert([1,3,5,6], 0)) # 0