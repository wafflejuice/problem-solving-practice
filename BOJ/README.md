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