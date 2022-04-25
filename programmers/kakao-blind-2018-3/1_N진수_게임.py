def solution(n, t, m, p):
    total_window_size = calc_total_window_size(t, m)
    window = ''
    window_size = 0
    num = 0
    while True:
        new_num_radix = num_to_radix(num, n)
        window += new_num_radix
        window_size += len(new_num_radix)
        num += 1
        if window_size >= total_window_size:
            break
            
    # print(window)
    
    curr_idx = p-1
    answer = window[curr_idx]
    remains = t-1
    while remains > 0:
        curr_idx += m
        answer += window[curr_idx]
        remains -= 1
        
    return answer

def calc_total_window_size(t, m):
    return t*m

def num_to_radix(num, radix):
    radix_table = '0123456789ABCDEF'
    if num == 0:
        return '0'
    
    num_by_radix = ''
    while num > 0:
        num_by_radix = radix_table[num % radix] + num_by_radix
        num //= radix
    return num_by_radix
    
    

sample_inputs = [
    [2, 4, 2, 1],
    [16, 16, 2, 1],
    [16, 16, 2, 2]
]

for s in sample_inputs:
    print(solution(s[0], s[1], s[2], s[3]))
    
# 2회차 : 20분