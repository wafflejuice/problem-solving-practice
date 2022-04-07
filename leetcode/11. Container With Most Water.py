class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_=self.max_area(height, 0, len(height)-1)
        return max_
        
    def max_area(self, height, begin, last):
        max_=0
        l,r=begin,last
        prehl,prehr=-1,-1
        while l<r:
            hl=height[l]
            hr=height[r]
            
            if hl<prehl:
                l+=1
                continue
            elif hr<prehr:
                r-=1
                continue
                
            area = (r-l)*min(hl, hr)
            max_ = max(max_, area)
                
            if hl==hr:
                if height[l+1] > height[r]:
                    l+=1
                elif height[l] < height[r-1]:
                    r-=1
                else:
                    l+=1
                    r-=1
            elif hl>hr:
                r-=1
            else:
                l+=1
            
            prehl=hl
            prehr=hr
        return max_
    
    def maxAreaTemp(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # [1,2].
        
        # 안쪽에 있는데 안 되면 괜찮다. (그보다 안쪽에 있는 건 고려할 필요 없다.)
        # 바깥에 있는데 안 되면 안 괜찮다.
        # 양쪽 바깥이 모두 안 돼야 끝?
        

print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(Solution().maxArea([1,1])) # 1
