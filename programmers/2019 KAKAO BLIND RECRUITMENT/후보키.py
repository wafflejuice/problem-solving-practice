def solution_slow(relation):
    from itertools import combinations

    valid_keys = []
    for key_size in range(1, len(relation[0])+1): # 1 <= key_size <= len(relation[0])
        for comb in combinations(range(len(relation[0])), key_size):
            comb = set(comb)
            tuples_set = set()
            for record in relation:
                new_tuple = tuple(record[i] for i in comb)
                if new_tuple in tuples_set:
                    break
                else:
                    tuples_set.add(new_tuple)
            else:
                valid_keys.append(comb)

    valid_idxes = [True for _ in range(len(valid_keys))]
    while True:
        is_updated = False
        for i in range(len(valid_keys)):
            if valid_idxes[i]:
                for j in range(i+1, len(valid_keys)):
                    if valid_idxes[j] and valid_keys[i] <= valid_keys[j]:
                        valid_idxes[j] = False
                        is_updated = True
        if not is_updated:
            break

    return len(list(filter(lambda x:x, valid_idxes)))

# By checking minimality before uniqueness,
# It is faster than previous solution.
def solution(relation):
    from itertools import combinations

    valid_keys = []
    for key_size in range(1, len(relation[0])+1): # 1 <= key_size <= len(relation[0])
        for comb in combinations(range(len(relation[0])), key_size):
            comb = set(comb)

            # minimality check
            for valid_key in valid_keys:
                if valid_key <= comb:
                    break
            else:
                tuples_set = set()
                for record in relation:
                    new_tuple = tuple(record[i] for i in comb)
                    if new_tuple in tuples_set:
                        break
                    else:
                        tuples_set.add(new_tuple)
                else:
                    valid_keys.append(comb)

    valid_idxes = [True for _ in range(len(valid_keys))]
    while True:
        is_updated = False
        for i in range(len(valid_keys)):
            if valid_idxes[i]:
                for j in range(i+1, len(valid_keys)):
                    if valid_idxes[j] and valid_keys[i] <= valid_keys[j]:
                        valid_idxes[j] = False
                        is_updated = True
        if not is_updated:
            break

    return len(list(filter(lambda x:x, valid_idxes)))

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
