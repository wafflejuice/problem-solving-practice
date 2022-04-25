def solution(words):
    Node.tot_cost = 0
    root_node = Node(words, 0)
    root_node.calc_children()
    # answer = root_node.calc_cost()
    answer = Node.tot_cost
    return answer

def check(words):
    tot_cnt = 0
    for word in words:
        cnt = 0
        for char_i in range(len(word)):
            cnt += 1
            candidates = []
            for candi_i in range(len(words)):
                if char_i < len(words[candi_i]) and word[char_i] == words[candi_i][char_i]:
                    candidates.append(words[candi_i])
            if len(candidates) <= 1:
                break
        tot_cnt += cnt
    return tot_cnt

class Node:
    tot_cost = 0
    
    def __init__(self, words, height):
        self.words = words
        self.children = []
        self.height = height
    
    def calc_children(self):
        if len(self.words) == 1:
            # print(f'At {self.words}, tot_cost += {self.height}')
            Node.tot_cost += self.height
            return
        elif '' in self.words:
            # print(f'At {self.words}, tot_cost += {self.height}')
            Node.tot_cost += self.height
            
        remaining_chars = {}
        for word in self.words:
            if len(word) > 0:
                if word[0] in remaining_chars.keys():
                    remaining_chars[word[0]].append(word[1:])
                else:
                    remaining_chars[word[0]] = [word[1:]]
        
        for k in remaining_chars.keys():
            child = Node(remaining_chars[k], self.height+1)
            child.calc_children()
            self.children.append(child)
    
    def calc_cost(self):
        if len(self.words) == 1:
            return self.height
        
        cost = 0
        if '' in self.words:
            cost += self.height
        for child in self.children:
            cost += child.calc_cost()
        return cost

sample_inputs = [
    ["go","gone","guild"],
    ["abc","def","ghi","jklm"],
    ["word","war","warrior","world"]
]

for s in sample_inputs:
    print(solution(s))

# 약 1시간27분