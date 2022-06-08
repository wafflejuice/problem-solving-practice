import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
truth_cnt, *truth_known = map(int, sys.stdin.readline().rstrip().split())

roots = [i for i in range(n+1)]
for t in truth_known:
    roots[t] = 0

def find(u):
    if u == roots[u]:
        return u
    roots[u] = find(roots[u])
    return roots[u]

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u == root_v:
        return
    if root_u == 0:
        roots[find(v)] = 0
    else:
        roots[find(u)] = root_v

parties = []
for _ in range(m):
    party_people_cnt, *party_people = map(int, sys.stdin.readline().rstrip().split())
    parties.append(party_people)
    for i in range(party_people_cnt-1):
        union(party_people[i], party_people[i+1])

cnt = 0
for pi in range(m):
    is_available = True
    for person in parties[pi]:
        if find(person) == 0:
            is_available = False
            break

    if is_available:
        cnt += 1

print(cnt)