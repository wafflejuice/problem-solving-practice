# ReDo List
- [[14500]테트로미노](https://www.acmicpc.net/problem/14500)  
Brute Force로 풀었지만, DFS로 풀 방법이 존재한다.

### [1389]케빈 베이컨의 6단계 법칙
Floyd-Warshall algorithm을 적당히 쓰고있던 나는 어째서인지 1회의 i,j,k 순환만에 최단경로들이 구해지지 않으면 while loop를 돌며 변화가 더이상 일어나지 않을 때까지 반복하고는 했다. 하지만 이는 잘못된 방법이다.  
Floyd-Warshall algorithm은 **가장 바깥 loop의 vertex가 두 지점 사이를 잇는 vertex**가 되어야 한다.
```python
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            new_w = graph[i][k] + graph[k][j]
            if new_w < graph[i][j]:
                graph[i][j] = new_w
```

### [2178]미로 탐색
sparse graph에서는 이웃 list로 구성하는 편이 (whole matrix를 저장하는 것보다) 빠르고 메모리를 적게 쓴다.  
가중치가 1로 고정되어 있으면 Dijkstra보다 BFS가 빠르다.

### [10026]적록색약
and, or 괄호를 제대로 안 닫아주는 초보적인 실수로 오답 제출. and가 or보다 우선순위가 높다.  
```python
# INCORRECT
if 0<=xi-1 and (matrix[yi][xi-1] == 'R' and matrix[yi][xi] == 'G') or (matrix[yi][xi-1] == 'G' and matrix[yi][xi] == 'R'):
    
# correct
if 0<=xi-1:
    if (matrix[yi][xi-1] == 'R' and matrix[yi][xi] == 'G') or (matrix[yi][xi-1] == 'G' and matrix[yi][xi] == 'R'):
        graph[yi * n + xi].append(yi * n + (xi-1))
        graph[yi * n + (xi-1)].append(yi * n + xi)
```

### [16236]아기 상어
2D matrix(mat[y][x]) 대신 1D matrix(mat[y*n+x])를 사용할 경우  

Pros)
1. tuple operation을 처리할 필요가 없어 편리하다.  

Cons)
1. 경계값을 구하기 번거롭다.
2. 자칫하면 2D와 비슷할 거라고 착각해 인접한 element 판별을 틀릴 수 있다.  

```python
# 1D
if v % n != 0:
    adjs.append(v-1)
if v % n != n - 1:
    adjs.append(v + 1)
if v // n != 0:
    adjs.append(v - n)
if v // n != n - 1:
    adjs.append(v + n)
```

### [9095]1, 2, 3 더하기
맞히고 나서 다른 사람들의 질문을 읽어보고 나서야 문제의 의도가 DP였다는 것을 알았다. DP가 아니라 순열로 풀었기 때문에 이래도 되나 싶은 묘한 감정이 든다. 나중에 DP로 다시 풀어볼 예정이다.  

### [1654]랜선 자르기
Parametric Search

### [9019]DSLR
BFS라는 것도 금방 깨달았고, 최적화도 금방 했지만 계속 시간 초과가 나서 접근 방식이 잘못된 줄 알았으나, PyPy3로 제출하니 성공했다. python으로는 못 푸는 문제 중 하나로 보인다.  

### [2162]선분 그룹
두 선분(l1, l2)에서 x 범위가 겹치는 부분 [a, b]을 구하고, x=a에서 l1의 y(sy1)와 l2의 y(sy2)를 비례식을 통해 구하고, 마찬가지로 x=b에서의 l1의 y(ey1)와 l2의 y(ey2)도 구해준 뒤, y값의 차이의 곱((sy1-sy2)*(ey1-ey2))이 0보다 작거나 같으면 교차한다고 판단하였다. 선분 i, j가 교차할 경우 간선이 존재하도록 graph를 만든 후 DFS를 통해 같은 group에 속하는지 판별하였다.  
다른 사람의 풀이를 찾아보니 모두 CCW와 union-find를 사용한 방법들만 나온다. 내 풀이가 모호하거나 잘못되었다고 생각하지는 않지만 기하 문제에서 CCW, union-find가 자주 사용되는 것으로 보이는 만큼, 해당 방법으로 다시 풀어볼 예정이다.  

### [14939]불 끄기
완전 탐색이라는 사실이 놀랍다. 다른 사람의 접근법을 읽지 않고서는 며칠 걸려도 못 풀었을 것 같다.  
매번 새로운 matrix의 copy를 사용해야 하는 것도 주의해야 할 부분이다.  

### [16566]카드 게임
union-find  
이진 탐색에서 unavailable value가 존재할 때 유용하다. unavailable idx가 자신의 우측에서 가장 작은 available idx를 parent로 갖도록 한다.  

### [14003]가장 긴 증가하는 부분 수열
LIS(Longest Increasing Subsequence) algorithm. Well-known이라고 한다.  
기본적인 전략은 DP이다. memo[i]는 i+1의 length를 가지는 subsequence 중 가장 작은 마지막 값이다. 이대로 풀면 O(n^2) time complexity를 가지므로, binary search를 사용해 O(n log n)로 줄여줘야 시간 효율성 테스트를 통과할 수 있다.  

### [2422]한윤정이 이탈리아에 가서 아이스크림을 사먹는데
Brute Force algorithm보다 나은 방법을 생각하느라 시간이 좀 걸렸지만 Brute Force로 풀리는 문제였다. Brute Force algorithm은 PS에서 사용하기 꺼려지는 측면이 있다.  

### [18111]마인크래프트
Python3라서 어려웠던 문제. 약간의 최적화를 거친 Brute Force로는 시간 초과가 나서 좀더 효율적인 방법으로 접근해 맞았으나, 그냥 초기 풀이를 PyPy3로 제출하면 맞는 문제였다.
