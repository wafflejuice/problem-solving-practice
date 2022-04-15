from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets=[]
        length=len(nums)
        for i in range(length):
            for j in range(i+1, length):
                fixed_sum=nums[i]+nums[j]
                low,high=j+1,length-1
                
                while low<high:
                    sum_ = fixed_sum+nums[low]+nums[high]
                    if sum_ == target:
                        new_quadruplet=(nums[i],nums[j],nums[low],nums[high])
                        if new_quadruplet not in quadruplets:
                            quadruplets.append(new_quadruplet)
                        low+=1
                        high-=1
                    elif sum_ < target:
                        low+=1
                    else:
                        high-=1
        
        return list(map(lambda x:list(x), quadruplets))

print(Solution().fourSum([1,0,-1,0,-2,2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(Solution().fourSum([2,2,2,2,2], 8)) # [[2,2,2,2]]
