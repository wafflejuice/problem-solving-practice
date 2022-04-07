import bisect

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        stones=sorted(stones)
        while len(stones)>=2:
            d=stones[-1]-stones[-2]
            stones=stones[:-2]
            if d>0:
                bisect.insort(stones, d)
        if len(stones)==0:
            return 0
        elif len(stones)==1:
            return stones[0]

print(Solution().lastStoneWeight([2,7,4,1,8,1])) # 1
print(Solution().lastStoneWeight([1])) # 1