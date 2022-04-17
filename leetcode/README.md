### 13. Roman to Integer
Leanrt "zip" usage
```
pair_dict = {i:j for i,j in zip(list1, list2)}
```
Roman to Integer는 문자열을 순회하며 i-1, i번째 원소의 대소비교로 쉽게 구현 가능

### 16. 3Sum Closest
useful O(N^2) algorithm for 3-sum-problem
```
        for i in range(len(nums)):
            lo,hi=i+1,len(nums)-1
            while lo<hi:
                sum_=nums[i]+nums[lo]+nums[hi]
                ...
                if sum_==target:
                    return target
                elif sum_>target:
                    hi-=1
                else:
                    lo+=1
```
(i<lo<hi) lo, hi로 양방향에서 좁혀오는 탐색

### 23. Merge k Sorted Lists
for sorting objects, use PriorityQueue instead of implementing binary insert yourself...
단, PriorityQueue에게 어떻게 정렬해야 할지 알려주기 위해 Wrapper class를 정의하고 Wrapper class를 활용한다.
- [ ] PriorityQueue를 사용해 재구현
```
from queue import PriorityQueue

class Wrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
        
q = PriorityQueue()
q.put(Wrapper(node))
```

k개의 sorted list를 merge하는 것은 Divide-and-Conquer를 사용해 푸는 것도 가능한 문제다.  
가령 a, b, c, d lists를 정렬할 때, a,b,c,d -> (a+b),(c+d) -> (a+b+c+d)
- [ ] Divide-and-Conquer 알고리즘으로 재구현

### 35. Search Insert Position
binary insertion
```python3
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
```

### 289. Game of Life
y, x 좌표로 표현되는 board에서 boundary check는 아래와 같이 간편하게 할 수 있다.  
즉, 각 위치마다 복잡한 if문으로 valid한지 따지지 않아도 된다.
```
for dy in [-1, 0, 1]:
    for dx in [-1, 0, 1]:
        if dy==0 and dx==0:
            continue
        ...
```
valid 여부만 따진다면, 다음과 같이 간편하게 구현할 수도 있다.
```
def is_valid(board, yi, xi):
    if (yi<0 or yi>=len(board) or xi<0 or xi>=len(board[0]):
        return False
    return True
```

### 538. Convert BST to Greater Tree
Wrapper를 사용해 특정 object를 쉽게 정렬할 수 있다.
```
class TreeNodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
```
BST to List는 Wrapper를 사용할 수도 있지만 느리고 메모리를 많이 쓴다.  
Wrapper를 안 쓰는 방법은 "99. Recover Binary Search Tree"를 참조.