def solution(n, t, m, timetable):
    bus_times = bus_schedule(n, t)
    crew_times = []
    for tt in timetable:
        crew_times.append(time_str_to(tt))
    crew_times = sort_times(crew_times)

    bi = 0
    ci = 0
    dic = {}
    while bi < len(bus_times):
        dic[tuple(bus_times[bi])] = []
        remains = m
        while ci < len(crew_times) and is_same_or_later(crew_times[ci], bus_times[bi]) and remains > 0:
            dic[tuple(bus_times[bi])].append(crew_times[ci])
            remains -= 1
            ci += 1
        bi += 1

    candidate = None
    if len(dic[tuple(bus_times[-1])]) < m:
        candidate = bus_times[-1]
    else:
        candidate = subtract(dic[tuple(bus_times[-1])][-1], 1)

    answer = time_prettify(candidate)
    return answer

def merge_sort(times):
    if len(times) <= 1:
        return times

    mid = len(times)//2
    left = merge_sort(times[:mid])
    right = merge_sort(times[mid:])

    li = 0
    ri = 0
    merged_list = []
    while li < len(left) and ri < len(right):
        if is_same_or_later(left[li], right[ri]):
            merged_list.append(left[li])
            li +=1
        elif is_same_or_later(right[ri], left[li]):
            merged_list.append(right[ri])
            ri += 1
        else:
            merged_list.append(left[li])
            merged_list.append(right[ri])
            li +=1
            ri+=1

    if li == len(left):
        merged_list += right[ri:]
    elif ri == len(right):
        merged_list += left[li:]

    return merged_list

def sort_times(times):
    return merge_sort(times)

def is_same_or_later(a, b):
    if a[0] < b[0]:
        return True
    if a[0] > b[0]:
        return False

    if a[1] < b[1]:
        return True
    if a[1] > b[1]:
        return False

    return True

def time_prettify(time):
    h = str(time[0])
    m = str(time[1])

    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m
    return h + ":" + m

def time_str_to(time):
    t=time.split(':')
    return [int(t[0]), int(t[1])]

def plus(time, minutes):
    time[1] += minutes
    if time[1] >= 60:
        time[0] += 1
        time[1] -= 60
    return time

def subtract(time, minutes):
    time[1] -= minutes
    if time[1] < 0:
        time[0] -= 1
        time[1] += 60
    return time

def bus_schedule(n, t):
    time = [9, 0]
    sch = [[9, 0]]
    for i in range(n-1):
        time = plus(time, t)
        sch.append(time.copy()) # IMPORTANT!!!
    return sch

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))

# 1시간30분은 걸렸다고 봐야 함.