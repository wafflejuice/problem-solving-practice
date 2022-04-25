def solution(dartResult):
    answer = 0

    dartResult = parse(dartResult)
    
    pre_score = 0
    curr_score, twice = calc_score(pre_score, dartResult[0])
    answer += curr_score

    pre_score = curr_score
    curr_score, twice = calc_score(pre_score, dartResult[1])
    answer += curr_score
    if twice:
        answer += pre_score

    pre_score = curr_score
    curr_score, twice = calc_score(pre_score, dartResult[2])
    answer += curr_score
    if twice:
        answer += pre_score
    
    return answer

def parse(dartResult):
    result = []
    prev_last = -1
    for i in range(len(dartResult)):
        if dartResult[i] in ['S', 'D', 'T']:
            if i+1 < len(dartResult) and dartResult[i+1] in ['*', '#']:
                if prev_last == -1:
                    result.append(dartResult[:i+1+1])
                else:
                    result.append(dartResult[prev_last+1:i + 1 + 1])
                prev_last = i+1
            else:
                if prev_last == -1:
                    result.append(dartResult[:i + 1])
                else:
                    result.append(dartResult[prev_last+1:i + 1])
                prev_last = i
    return result

def calc_score(pre_score, shoot):
    pre_score_twice = False
    score = 0
    bonus_idx = -1
    for i in range(len(shoot)):
        if shoot[i].isalpha():
            bonus_idx = i
            score = int(shoot[:i])
            break
    
    if shoot[bonus_idx] == 'D':
        score = score ** 2
    elif shoot[bonus_idx] == 'T':
        score = score ** 3
    
    if shoot[-1] in ['S', 'D', 'T']:
        return score, False
    
    if shoot[-1] == '*':
        score *= 2
        pre_score_twice = True
    else:
        score = -score
    
    return score, pre_score_twice

sample_inputs = ['1S2D*3T','1D2S#10S','1D2S0T','1S*2T*3S','1D#2S*3S','1T2D3D#','1D2S3T*']

for s in sample_inputs:
    print(solution(s))
    
import re
p = re.compile('[0-9]+[SDT][*#]?')
for s in sample_inputs:
    m = p.findall(s)
    print(f's={s}\t\t m={m}')
print()

# 카카오 블라인드 2018년 1차 다 푸는데 간당간당하게 5시간