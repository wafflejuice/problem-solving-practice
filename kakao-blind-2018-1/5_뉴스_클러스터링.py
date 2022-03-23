def solution(str1, str2):
    answer = jacard(multiset(str1), multiset(str2))
    return answer

def multiset(string):
    s = []
    for i in range(len(string)-1):
        t = string[i] + string[i+1]
        if t.isalpha():
            s.append(t.lower())
    return s

def jacard(set1, set2):
    cnt = 0
    
    if len(set1) == len(set2) == 0:
        return 1 * 65536
    
    for i in range(len(set1)):
        for j in range(len(set2)):
            if set1[i] is not None and set2[j] is not None and set1[i] == set2[j]:
                cnt+=1
                set1[i] = None
                set2[j] = None
    
    return int(cnt / (len(set1) + len(set2) - cnt) * 65536)

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2	', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))

# 15분컷