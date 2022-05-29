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
