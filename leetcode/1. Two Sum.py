class Solution(object):
    def binary_search(self, arr, target, low_in, high_ex):
        while low_in < high_ex:
            mid = (high_ex + low_in) // 2

            if arr[mid] < target:
                low_in = mid+1
            elif arr[mid] > target:
                high_ex = mid
            else:
                return mid
        
        return -1
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        sorted_nums_indices = sorted(range(len(nums)), key=lambda x: nums[x])
        nums.sort()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            idx = self.binary_search(nums, complement, 0, len(nums))
            if idx == -1 or idx == i:
                continue
            return sorted_nums_indices[i], sorted_nums_indices[idx]
            
print(Solution().twoSum([3,2,3], 6))