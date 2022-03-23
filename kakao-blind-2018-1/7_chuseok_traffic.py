def calc(times):
    max_cnt = 0
    for t in times:
        start_time = t[1]  # end_time
        cnt = inside_cnt(start_time, times)
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt
def inside_cnt(frame, times):
    range = [0, 0, 1, 0]
    cnt = 0
    for t in times:
        start_time = t[0]
        end_time = t[1]
        
        start_time_b = frame
        end_time_b = plus(frame, range)
        
        # print(f'start_time={start_time}, end_time={end_time}, start_time_b={start_time_b}, end_time_b={end_time_b}')
        if not (bigger(end_time, start_time_b) or (bigger(end_time_b, start_time))):
            # print('cnt++')
            cnt += 1
    return cnt
def bigger(a, b):
    if a[0] < b[0]:
        return True
    if a[0] > b[0]:
        return False
    
    if a[1] < b[1]:
        return True
    if a[1] > b[1]:
        return False
    
    if a[2] < b[2]:
        return True
    if a[2] > b[2]:
        return False
    
    if a[3] < b[3]:
        return True
    if a[3] > b[3]:
        return False
    
    return False
def calc_time(line):
    ttt = line.split()
    end_time = ttt[1]
    elapsed_time = ttt[2]
    end_hh, end_mm, end_sssss = end_time.split(':')
    end_ss, end_ms = end_sssss.split('.')
    
    end_time = [end_hh, end_mm, end_ss, end_ms]
    end_time = time_to_int(end_time)
    
    elapsed_time = elapsed_time[:-1]
    if '.' in elapsed_time:
        elapsed_ss, elapsed_ms = elapsed_time.split('.')
    else:
        elapsed_ss = elapsed_time
        elapsed_ms = '000'
    elapsed_ms = prettify(elapsed_ms)
    
    elapsed_time = [elapsed_ss, elapsed_ms]
    elapsed_time = time_to_int(elapsed_time)
    
    start_time = subtract(end_time, elapsed_time)
    
    return [start_time, end_time]
def prettify(ms):
    while True:
        if len(ms) == 3:
            break
        else:
            ms += "0"
    return ms
def time_to_int(time):
    r = []
    for i in range(len(time)):
        r.append(int(time[i]))
    return r
def subtract(time, amount):
    end_hh = time[0]
    end_mm = time[1]
    end_ss = time[2]
    end_ms = time[3]
    
    amount_hh = 0
    amount_mm = 0
    
    if len(amount) == 2:
        amount_ss = amount[0]
        amount_ms = amount[1]
    else:
        amount_ss = amount[2]
        amount_ms = amount[3]
    
    end_ms += 1
    
    end_ms -= amount_ms
    while end_ms < 0:
        end_ss -= 1
        end_ms += 1000
    
    end_ss -= amount_ss
    while end_ss < 0:
        end_mm -= 1
        end_ss += 60
    
    end_mm -= amount_mm
    while end_mm < 0:
        end_hh -= 1
        end_mm += 60
    
    end_hh -= amount_hh
    
    return [end_hh, end_mm, end_ss, end_ms]
def plus(time, amount):
    start_hh = time[0]
    start_mm = time[1]
    start_ss = time[2]
    start_ms = time[3]
    
    amount_hh = 0
    amount_mm = 0
    
    if len(amount) == 2:
        amount_ss = amount[0]
        amount_ms = amount[1]
    else:
        amount_ss = amount[2]
        amount_ms = amount[3]
    
    start_ms -= 1
    
    start_ms += amount_ms
    while start_ms >= 1000:
        start_ss += 1
        start_ms -= 1000
    
    start_ss += amount_ss
    while start_ss >= 60:
        start_mm += 1
        start_ss -= 60
    
    start_mm += amount_mm
    while start_mm >= 60:
        start_hh += 1
        start_mm -= 60
    
    start_hh += amount_hh
    
    return [start_hh, start_mm, start_ss, start_ms]
def solution(lines):
    answer = 0
    
    times = []
    for line in lines:
        times.append(calc_time(line))
    
    answer = calc(times)
    
    return answer
# print(
# solution(  [
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]
# )
# )

#1h17 걸림