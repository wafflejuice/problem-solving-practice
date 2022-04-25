def solution(id_list, report, k):
    report = list(set(report))
    report = list(map(lambda x: x.split(), report))

    target_count = dict()
    for id in id_list:
        target_count[id] = 0
    for r in report:
        target_count[r[1]] += 1

    stop_list = []
    for key, value in target_count.items():
        if value >= k:
            stop_list.append(key)

    notify_count = dict()
    for id in id_list:
        notify_count[id] = 0
    for r in report:
        if r[1] in stop_list:
            notify_count[r[0]] += 1

    answer = []
    for id in id_list:
        answer.append(notify_count[id])

    return answer