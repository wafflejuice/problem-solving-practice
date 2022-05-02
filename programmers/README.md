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
print(sorted(d.items(), key=lambda x:x[1])) # [1, 3, 2]
```