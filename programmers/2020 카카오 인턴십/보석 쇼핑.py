# Fourth approach
# Multi-pointer, using binary search, compare only the first finger and the last finger
# all success
def solution(gems):
    import bisect
    from collections import deque

    gem_idxes_dict=dict()
    for idx, gem in enumerate(gems):
        if gem not in gem_idxes_dict:
            gem_idxes_dict[gem] = deque()
        gem_idxes_dict[gem].append(idx)

    fingers = []
    for gem, idxes in gem_idxes_dict.items():
        bisect.insort_left(fingers, idxes[0])

    shortest_range = [1, len(gems)]
    shortest_length = len(gems)
    while True:
        min_idx = fingers[0]
        min_gem = gems[min_idx]
        max_idx = fingers[-1]

        if max_idx - min_idx + 1 < shortest_length:
            shortest_range = [min_idx + 1, max_idx + 1]
            shortest_length = max_idx - min_idx + 1

        fingers.pop(0)
        gem_idxes_dict[min_gem].popleft()
        if len(gem_idxes_dict[min_gem]) == 0:
            break

        bisect.insort_left(fingers, gem_idxes_dict[min_gem][0])

    return shortest_range


# Third approach
# Multi-pointer, use one dictionary with deque
# time efficiency test score = 4/15
def solution_Multipointer_2(gems):
    from collections import deque

    gem_idxes_dict=dict()
    for idx, gem in enumerate(gems):
        if gem not in gem_idxes_dict:
            gem_idxes_dict[gem] = deque()
        gem_idxes_dict[gem].append(idx)

    shortest_range = [1, len(gems)]
    shortest_length = len(gems)
    while True:
        min_gem=None
        min_idx, max_idx = 100001, -1
        for gem, idxes in gem_idxes_dict.items():
            if len(gem_idxes_dict[gem]) == 0:
                return shortest_range

            idx = gem_idxes_dict[gem].popleft()

            if idx < min_idx:
                min_gem = gem
                min_idx = idx
            if idx > max_idx:
                max_idx = idx

            gem_idxes_dict[gem].appendleft(idx)

        if max_idx - min_idx + 1 < shortest_length:
            shortest_range = [min_idx + 1, max_idx + 1]
            shortest_length = max_idx - min_idx + 1

        gem_idxes_dict[min_gem].popleft()


# Second approach
# Multi-pointer, use two dictionaries
# time efficiency test score = 5/15
def solution_Multipointer_1(gems):
    gem_idxes_dict=dict()
    for idx, gem in enumerate(gems):
        if gem not in gem_idxes_dict:
            gem_idxes_dict[gem] = []
        gem_idxes_dict[gem].append(idx)

    gem_finger_dict=dict()
    for gem in gem_idxes_dict.keys():
        gem_finger_dict[gem]=0

    shortest_range = [1, len(gems)]
    shortest_length = len(gems)
    while True:
        min_gem=None
        min_idx, max_idx = 100001, -1
        for gem, finger in gem_finger_dict.items():
            if gem_idxes_dict[gem][finger] < min_idx:
                min_gem = gem
                min_idx = gem_idxes_dict[gem][finger]
            if gem_idxes_dict[gem][finger] > max_idx:
                max_idx = gem_idxes_dict[gem][finger]

        if max_idx - min_idx + 1 < shortest_length:
            shortest_range = [min_idx + 1, max_idx + 1]
            shortest_length = max_idx - min_idx + 1

        gem_finger_dict[min_gem] += 1
        if gem_finger_dict[min_gem] == len(gem_idxes_dict[min_gem]):
            break

    return shortest_range


# First approach
# DP like sliding window
# time efficiency failed (0/15)
def solution_DP(gems):
    types_cnt = len(set(gems))
    gems_length = len(gems)

    memo=[]
    for i in range(gems_length):
        memo.append([])

    shortest_range, shortest_length = None, 100001
    for i in range(gems_length):
        tmp=set()
        for j in range(i, min(gems_length, i+shortest_length-1)):
            if gems[j] in tmp:
                memo[i].append(memo[i][-1])
                continue

            tmp.add(gems[j])
            if i==j:
                memo[i].append(1)
            else:
                memo[i].append(memo[i][-1] + 1)

            if memo[i][j-i] == types_cnt:
                shortest_range = (i,j)
                shortest_length = j-i+1
                break

    return shortest_range[0] + 1, shortest_range[1] + 1

inputs=[
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"], 	#[3, 7]
    ["AA", "AB", "AC", "AA", "AC"], 	#[1, 3]
    ["XYZ", "XYZ", "XYZ"], 	#[1, 1]
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"] 	#[1, 5]
]

for input_ in inputs:
    print(solution(input_))