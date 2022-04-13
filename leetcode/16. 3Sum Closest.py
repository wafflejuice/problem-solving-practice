from typing import *
import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_delta=math.inf
        ans=0
        for i in range(len(nums)):
            lo,hi=i+1,len(nums)-1
            while lo<hi:
                sum_=nums[i]+nums[lo]+nums[hi]
                if abs(sum_-target) < min_delta:
                    min_delta = abs(sum_-target)
                    ans=sum_
                if sum_==target:
                    return target
                elif sum_>target:
                    hi-=1
                else:
                    lo+=1
        return ans

print(Solution().threeSumClosest([-1,2,1,-4], 1)) # 2
print(Solution().threeSumClosest([0,0,0], 1)) # 0