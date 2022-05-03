def solution_recursive(n, path, order):
    link_dict = dict()
    order_dict = dict()
    
    def dfs(node, visit):
        if len(order_dict) == 0:
            return True
        if node in visit:
            return False
        if node in order_dict.values():
            return False
    
        visit.add(node)
        if node in order_dict.keys():
            order_dict.pop(node)
            
        if node != 0 and len(link_dict[node]) == 1:
            link_dict[link_dict[node][0]].remove(node)
            link_dict.pop(node)
        elif node != 0 and len(link_dict[node]) == 2:
            unvisit_node = None
            for li, neighbor in enumerate(link_dict[node]):
                if neighbor not in visit:
                    unvisit_node = neighbor
                link_dict[neighbor].remove(node)
                link_dict[link_dict[node][li]].append(link_dict[node][1-li])
            link_dict.pop(node)
            node = unvisit_node
            if dfs(node, visit):
                return True
        else:
            for next_node in link_dict[node][:]: # to remove while enumerating
                if dfs(next_node, visit):
                    return True
    
        return False
    
    # first approach : recursive DFS with shrink
    # time efficiency fail
    def solution(n, path, order):
        for i in range(n):
            link_dict[i] = []
            
        for pair in path:
            link_dict[pair[0]].append(pair[1])
            link_dict[pair[1]].append(pair[0])
        
        for pair in order:
            order_dict[pair[0]] = pair[1] # first:second
        
        while True:
            init_len = len(order_dict)
            dfs(0, set())
            if init_len == len(order_dict):
                break
        
        return len(order_dict) == 0
    
    return solution(n, path, order)

# second approach: non-recursive DFS with shrink
# time efficiency fail
def solution2(n, path, order):
    from collections import deque
    
    link_dict = dict()
    order_dict = dict()
    
    for i in range(n):
        link_dict[i] = []
        
    for pair in path:
        link_dict[pair[0]].append(pair[1])
        link_dict[pair[1]].append(pair[0])
    
    for pair in order:
        order_dict[pair[0]] = pair[1] # first:second
    
    while True:
        is_changed = False
        stack = deque([0])
        visit = set()
        while len(stack) > 0:
            if len(order_dict) == 0:
                return True
            
            node = stack.pop()
            if node in visit:
                continue
            if node in order_dict.values():
                continue
    
            visit.add(node)
            if node in order_dict.keys():
                order_dict.pop(node)
                is_changed = True
    
            if node != 0 and len(link_dict[node]) == 1:
                link_dict[link_dict[node][0]].remove(node)
                link_dict.pop(node)
            elif node != 0 and len(link_dict[node]) == 2:
                unvisit_node = None
                for li, neighbor in enumerate(link_dict[node]):
                    if neighbor not in visit:
                        unvisit_node = neighbor
                    link_dict[neighbor].remove(node)
                    link_dict[link_dict[node][li]].append(link_dict[node][1 - li])
                link_dict.pop(node)
                stack.append(unvisit_node)
            else:
                for next_node in link_dict[node][:]:  # to remove while enumerating
                    stack.append(next_node)
        
        if not is_changed:
            break
    
    return len(order_dict) == 0

# Topology sort
def solution(n, path, order):
    from collections import deque
    
    parent_children = [[] for _ in range(n)]
    indegree = dict()
    for i in range(n):
        indegree[i] = 0

    for a, b in path:
        parent_children[a].append(b)
        parent_children[b].append(a)
    
    # tree generation with indegree cnt?
    # tree generation, then indegree cnt?
    
    for pair in order:
        parent_children[pair[0]].append(pair[1])
        indegree[pair[1]] += 1
    
    visit_cnt = 0
    q = deque([0])
    while len(q) > 0:
        node = q.popleft()
        visit_cnt += 1
        for child in parent_children[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)
        
    return visit_cnt == n
    
    
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]])) # true
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]])) # true
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]])) # false

print(solution(12, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5],[6,9],[9,10],[10,11]], [[8,5],[6,7],[4,1]])) # true