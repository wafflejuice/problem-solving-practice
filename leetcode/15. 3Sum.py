from typing import *
import bisect

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positives,negatives=[],[]
        zero_cnt=0
        for n in nums:
            if n>0:
                bisect.insort(positives, n)
            elif n<0:
                bisect.insort(negatives, n)
            else:
                zero_cnt += 1
        
        triplets=[]
        
        # no zero
        self.calc_two_one(triplets, positives, negatives)
        self.calc_two_one(triplets, negatives, positives)
        
        # one zero
        if zero_cnt >= 1:
            for i in range(len(positives)):
                neg_idx = bisect.bisect_left(negatives, -positives[i])
                if neg_idx<len(negatives) and negatives[neg_idx] == -positives[i]:
                    triplets.append((negatives[neg_idx], 0, positives[i]))
                
        # three zeros
        if zero_cnt >= 3:
            triplets.append((0, 0, 0))
            
        triplets = list(map(lambda x:list(x), set(triplets)))
        
        return triplets
        
    def calc_two_one(self, three, two, one):
        for i in range(len(two)):
            for j in range(i+1, len(two)):
                sum_=two[i]+two[j]
                idx=bisect.bisect_left(one, -sum_)
                if idx<len(one) and one[idx] == -sum_:
                    three.append(tuple(sorted([two[i], two[j], one[idx]])))

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([]))
print(Solution().threeSum([0]))