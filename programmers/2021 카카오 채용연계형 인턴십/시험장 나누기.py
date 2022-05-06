class Node:
    def __init__(self, uid, val, parent, left, right):
        self.uid = uid
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        if self.val < other.val:
            return True
        return False
    
    def accumulate(self, leader_uids):
        acc = 0
        is_accumulable = self.uid not in leader_uids
        if self.left:
            if self.left.accumulate(leader_uids):
                acc += self.left.val
                self.left.parent = None
                self.left.val = None
                self.left = None
            else:
                is_accumulable = False
        if self.right:
            if self.right.accumulate(leader_uids):
                acc += self.right.val
                self.right.parent = None
                self.right.val = None
                self.right = None
            else:
                is_accumulable = False
        self.val += acc
        
        return is_accumulable
    
    def count(self):
        cnt = 1
        if self.left:
            cnt += self.left.count()
        if self.right:
            cnt += self.right.count()
        return cnt
    
    def find(self, uid):
        if self.uid == uid:
            return self
        if self.left:
            found = self.left.find(uid)
            if found:
                return found
        if self.right:
            found = self.right.find(uid)
            if found:
                return found
        return None
    
    def tree(self):
        res = [self]
        if self.left:
            res += self.left.tree()
        if self.right:
            res += self.right.tree()
        return res
        
def solution(k, num, links):
    import heapq
    
    # 1. tree gen
    
    # 2. calc mean
    
    # 3. find nodes where val >= mean
    
    # 4. 대장 없는 subtree를 가지는 node는 parent에게 흡수
    
    # k개 남을 때까지 2, 3, 4 반복
    
    nodes = [Node(i, num[i], None, None, None) for i in range(len(num))]
    sum_ = sum(num)
    print(f'sum_={sum_}')
    for i in range(len(links)):
        if links[i][0] != -1:
            nodes[i].left = nodes[links[i][0]]
            nodes[links[i][0]].parent = nodes[i]
        if links[i][1] != -1:
            nodes[i].right = nodes[links[i][1]]
            nodes[links[i][1]].parent = nodes[i]
            
    root = None
    for node in nodes:
        if node.parent is None:
            root = node
            break
    
    while True:
        nodes = root.tree()
        node_cnt = len(nodes)
        mean = sum_ / node_cnt

        print(f'sum_={sum_}, node_cnt={node_cnt}, mean={mean}')
        
        if node_cnt >=k:
            pass
        else:
            pass
        
        leader_uids = []
        for i in range(len(nodes)):
            if nodes[i].val > mean:
                leader_uids.append(nodes[i].uid)
                
        print(leader_uids)
        
        print_tree(root)
        print()
        
        if len(leader_uids) >= k:
            root.accumulate(leader_uids)
            
            print_tree(root)
            print()
        else:
            delta = node_cnt - k
            heapq.heapify(nodes)
            i = 0
            while i < delta:
                node = heapq.heappop(nodes)
                res = []
                if node.parent:
                    res.append((node.parent, 0))
                if node.left:
                    res.append((node.left, 1))
                if node.right:
                    res.append((node.right, 2))
                
                if len(res) == 0:
                    pass
                else:
                    sss = sorted(res)[0]
                    if sss[1] == 0:
                        sss[0]
                    if sss[1] == 1:
                        pass
                    if sss[1] == 2:
                        pass
                    i += 1
                    
        
    answer = 0
    return answer

def print_tree(root):
    if root is None:
        print('None', end=', ')
        return
    else:
        print(root.val, end=', ')
    print_tree(root.left)
    print_tree(root.right)

print(solution(3,	[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],	[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))