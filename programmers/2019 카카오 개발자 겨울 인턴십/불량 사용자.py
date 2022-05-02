import re

def dfs(banned_id, bi_idx, uid_remains, bu_pair, path, whole_paths):
    if bi_idx == len(banned_id):
        whole_paths.add(tuple(sorted(path)))
        return

    cur = banned_id[bi_idx]
    for uid in bu_pair[cur]:
        if uid in uid_remains:
            uid_remains.remove(uid)
            dfs(banned_id, bi_idx + 1, uid_remains, bu_pair, path+[uid], whole_paths)
            uid_remains.append(uid)

def solution(user_id, banned_id):
    banned_id = list(map(lambda x:x.replace('*', '.'), banned_id))
    bu_pair = dict()
    for bid in set(banned_id):
        for uid in user_id:
            p = re.compile('^'+bid+'$')
            sid = p.search(uid)
            if sid:
                if bid not in bu_pair:
                    bu_pair[bid] = []
                bu_pair[bid].append(uid)

    banned_ids_set = set()
    dfs(banned_id, 0, user_id.copy(), bu_pair, [], banned_ids_set)
    return len(banned_ids_set)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) #	2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) #	2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) #	3))