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