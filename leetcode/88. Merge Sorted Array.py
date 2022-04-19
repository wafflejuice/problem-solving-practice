from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        merged_nums=[]
        i,j=0,0
        while i<m and j<n:
            if nums1[i] <= nums2[j]:
                merged_nums.append(nums1[i])
                i+=1
            else:
                merged_nums.append(nums2[j])
                j+=1
                
        while i<m:
            merged_nums.append(nums1[i])
            i += 1
            
        while j<n:
            merged_nums.append(nums2[j])
            j += 1
        
        for i in range(m+n):
            nums1[i] = merged_nums[i]
            
arr1=[1,2,3,0,0,0]
Solution().merge(nums1 = arr1, m = 3, nums2 = [2,5,6], n = 3) # [1,2,2,3,5,6]
print(arr1)

arr2=[1]
Solution().merge(nums1 = arr2, m = 1, nums2 = [], n = 0) # [1]
print(arr2)

arr3=[0]
Solution().merge(nums1 = arr3, m = 0, nums2 = [1], n = 1) # [1]
print(arr3)