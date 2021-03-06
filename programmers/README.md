# ReDo List
- [2019 KAKAO BLIND RECRUITMENT/실패율](https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3)  
Time efficiency가 아슬아슬했다.
- [2020 카카오 인턴십/보석 쇼핑](https://programmers.co.kr/learn/courses/30/lessons/67258)  
Time efficiency test를 몇 번이고 실패한 끝에 성공했으나 풀이가 간결하지 않다. multi-pointer algorithm으로 풀었는데 two pointer algorithm으로도 가능하다.
- [2019 카카오 개발자 겨울 인턴십/불량 사용자](https://programmers.co.kr/learn/courses/30/lessons/64064)  
itertools.product 활용해보기

### 2019 카카오 개발자 겨울 인턴십/불량 사용자
banned_id가 될 수 있는 user_id가 여러 개 존재하고, banned_id와 user_id를 match하면 이후에는 해당 user_id를 사용할 수 없으므로 DFS로 풀었다.
하지만 itertools.product()를 사용하면 좀더 간단하게 풀 수 있다.  

itertools.product의 사용예시)
```python
import itertools

l = [[1,2,3], [4, 5]]
list(itertools.product(*l)) # [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
```

sorted()는 list, tuple뿐만 아니라 set, dict에도 적용할 수 있다. 반환된 결과는 list이다.
```python
s = {1, 3, 2}
print(sorted(s)) # [1, 2, 3]
d = {1:'a', 3:'b', 2:'c'}
print(sorted(d)) # [1, 2, 3]
print(sorted(d.items(), key=lambda x:x[1])) # [(1, 'a'), (3, 'b'), (2, 'c')]
```

### 2020 카카오 인턴십/동굴 탐험
자꾸 헷갈려 하는데 DFS에서 stack은 non-recursive할 때만 사용한다.  
recursive DFS 코드가 길어지면... 뭔가 잘못됐다!

```python
def dfs(v, visit):
    if v in visit:
        return
    visit.append(v)
    for neighbor in links[v]:
        dfs(neighbor, visit)

dfs(start_v)
```

Topology sort
```python
q = deque([0])
visit = []
while len(q) > 0:
    node = q.popleft()
    visit.append(node)
    for child in children_of[node]:
        indegree[child] -= 1
        if indegree[child] == 0:
            q.append(child)
print(visit) # Topology sorted
```

dict도 좋지만 key가 정수이고 밀집되어 있다면 list도 고려해봄직 하다.
```python
a = dict()
a[0] = ['a', 'b']
a[1] = ['c']
...
# {0:['a', 'b'], 1:['c'], ...}

b = []
b[0] = ['a', 'b']
b[1] = ['c']
...
# [['a', 'b'], ['c'], ...]
```

### 2019 KAKAO BLIND RECRUITMENT/후보키
set 종속관계 판별
```python
# check if set1 is a subset of set2
set1 = {0, 1, 4, 2}
set2 = {5, 4, 2, 0, 1}
print(set1 <= set2) # correct
print(set1 in set2) # NOT correct
```

### 2021 카카오 채용연계형 인턴십/표 편집
정확성 테스트는 1시간 내로 구현했으나 시간 효율성 테스트에 수 시간이 소요된 문제.  
python에서 linked list를 간이 구현하는 경험을 할 수 있다. list에서 O(n)인 append, pop을 제거하는 것이 관건이었다. (bisect를 사용하더라도 search가 O(log n)으로 줄어드는 것이지 insert, delete는 여전히 O(n)이다.)  
list의 모든 element가 자신의 **유효한** 이전 element와 **유효한** 다음 element를 저장하도록 하여 O(n)을 O(1)으로 줄였다.  
굳이 python 내장 list에 잡다한 정보를 넣는 것보단 LinkedList 같은 user class를 정의하는 편이 더 가독성 좋고 이해하기 쉬웠을 것 같다.
