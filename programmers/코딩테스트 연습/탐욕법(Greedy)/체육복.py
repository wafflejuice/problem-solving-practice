def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    i = 0
    while i < len(lost):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost.pop(i)
            continue
        i += 1

    i = 0
    while i < len(lost):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            lost.pop(i)
            continue
        if lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            lost.pop(i)
            continue

        i += 1

    return n - len(lost)

print(solution(5,	[2, 4],	[1, 3, 5])) # 5
print(solution(5,	[2, 4],	[3])) # 4
print(solution(3,	[3],	[1])) # 2