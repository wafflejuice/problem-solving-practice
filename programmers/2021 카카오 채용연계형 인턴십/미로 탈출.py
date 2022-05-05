import math
import heapq

def solution(n, start, end, roads, traps):
    trap_states_cnt = 2**len(traps)
    graph = [[[[math.inf for _ in range(n+1)] for _ in range(n+1)] for _ in range(trap_states_cnt)] for _ in range(trap_states_cnt)]

    bitmask = trap_states_cnt-1
    for a, b, w in roads:
        for from_state in range(trap_states_cnt):
            is_from_trap = a in traps
            is_to_trap = b in traps

            to_state = from_state
            
            if is_from_trap and is_to_trap:
                # to_state &= (1 << traps.index(a)) ^ bitmask
                to_state |= (1 << traps.index(b))
                
                is_from_on = from_state & (1 << traps.index(a))
                is_to_on = from_state & (1 << traps.index(b))
                if is_from_on and is_to_on:
                    graph[from_state][to_state][a][b] = w
                    graph[to_state][from_state][b][a] = w
                elif is_from_on and not is_to_on:
                    # graph[to_state][from_state][b][a] = w
                    pass
                elif not is_from_on and is_to_on:
                    graph[to_state][from_state][b][a] = w
                elif not is_from_on and not is_to_on:
                    graph[from_state][to_state][a][b] = w
            elif is_from_trap and not is_to_trap:
                to_state &= (1 << traps.index(a)) ^ bitmask
                is_from_on = from_state & (1 << traps.index(a))
                if is_from_on:
                    graph[to_state][from_state][b][a] = w
                else:
                    graph[from_state][to_state][a][b] = w
            elif not is_from_trap and is_to_trap:
                to_state |= (1 << traps.index(b))
                is_to_on = from_state & (1 << traps.index(b))
                if is_to_on:
                    graph[to_state][from_state][b][a] = w
                else:
                    graph[from_state][to_state][a][b] = w
            else:
                graph[from_state][to_state][a][b] = w
            
    for from_state in range(trap_states_cnt):
        for v in range(1, n+1):
            graph[from_state][from_state][v][v] = 0
    
    dist = [[math.inf for _ in range(n+1)] for _ in range(trap_states_cnt)]
    dist[0][start] = 0
    
    priority_q = [(0, 0, start)]
    heapq.heapify(priority_q)
    
    while len(priority_q) > 0:
        cur_dist, from_state, v = heapq.heappop(priority_q)
        print()
        print(f'dist={dist}')
        print(f'cur_dist={cur_dist}, trap_state={from_state}, v={v}')

        if v in traps:
            from_state &= (1 << traps.index(v)) ^ bitmask
        
        import time
        time.sleep(0.3)
        for neighbor in range(1, n+1):
            for to_state in range(len(traps)):
                if graph[from_state][to_state][v][neighbor] < math.inf:
                    new_dist = cur_dist + graph[from_state][to_state][v][neighbor]
                    
                    next_trap_state = from_state
                    
                    if neighbor in traps:
                        next_trap_state |= (1 << traps.index(neighbor))
                        
                    old_dist = dist[from_state][neighbor]
                    print(f'neighbor={neighbor}, old_dist={old_dist}, new_dist={new_dist}')
                    
                    if new_dist < old_dist:
                        print(f'relax dist[{next_trap_state}][{neighbor}] from {dist[next_trap_state][neighbor]} to {new_dist}')
                        dist[next_trap_state][neighbor] = new_dist
                        heapq.heappush(priority_q, (new_dist, next_trap_state, neighbor))
    
    min_end_dist = math.inf
    for from_state in range(trap_states_cnt):
        min_end_dist = min(min_end_dist, dist[from_state][end])
        print(f'dist[{from_state}][{end}]={dist[from_state][end]}')
        
    return min_end_dist

print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])) # 5
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])) # 4