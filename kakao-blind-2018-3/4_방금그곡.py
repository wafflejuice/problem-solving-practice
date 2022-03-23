import re

def solution(m, musicinfos):
    m = music_to_notes(m)
    
    splited_musicinfos = []
    for musicinfo in musicinfos:
        splited_musicinfos.append(split_musicinfo(musicinfo))
    for sm in splited_musicinfos:
        sm[0] = time_str_to_list(sm[0])
        sm[1] = time_str_to_list(sm[1])
        notes = music_to_notes(sm[3])
        sm[3] = notes
        
    core_infos = []
    for sm in splited_musicinfos:
        extended_notes = extend_notes(sm[0], sm[1], sm[3])
        core_infos.append([sm[2], extended_notes])
    
    candidates = []
    for c in core_infos:
        if check_contain(m, c[1]):
            candidates.append(c)
    
    if len(candidates) == 0:
        answer = '(None)'
    elif len(candidates) == 1:
        answer = candidates[0][0]
    else:
        longest_length = -1
        longest_idx = -1
        for ci in range(len(candidates)):
            if len(candidates[ci][1]) > longest_length:
                longest_length = len(candidates[ci][1])
                longest_idx = ci
        answer = candidates[longest_idx][0]
        
    return answer

def check_contain(m, notes):
    for ni in range(len(notes)-len(m)+1):
        is_containing = True
        for mi in range(len(m)):
            if notes[ni+mi] != m[mi]:
                is_containing = False
                break
        if is_containing:
            return True
    return False

def time_str_to_list(time):
    HH, MM = time.split(':')
    return [int(HH), int(MM)]

def extend_notes(start_time, end_time, notes):
    play_time = subtract(end_time, start_time)
    play_minues = play_time[0] * 60 + play_time[1]
    
    extended_notes = notes * (play_minues // len(notes))
    extended_notes += notes[:play_minues % len(notes)]
    
    return extended_notes

def subtract(time1, time2):
    time1[1] -= time2[1]
    if time1[1] < 0:
        time1[0] -= 1
        time1[1] += 60
    time1[0] -= time2[0]
    
    return time1

def split_musicinfo(musicinfo):
    start_time, end_time, title, music = musicinfo.split(',')
    return [start_time, end_time, title, music]

def music_to_notes(music):
    p = re.compile('[A-Z][#]?')
    notes = p.findall(music)
    
    return notes

sample_inputs = [
    ["ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]],
    ["CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]],
    ["ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]]
]

for s in sample_inputs:
    print(solution(s[0], s[1]))
    
# 2회차 : 39분