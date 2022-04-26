import re

def solution(s):
    p=re.compile("{[0-9,]+}")
    sets=[]
    for element in p.findall(s):
        sets.append(set(map(lambda x:int(x), element[1:-1].split(','))))
    sets.sort(key=lambda x:len(x))
    
    answer = list(sets[0])
    for si in range(len(sets)-1):
        answer.append(list(sets[si+1].difference(sets[si]))[0])
        
    return answer

inputs = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",	#[2, 1, 3, 4]
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",	#[2, 1, 3, 4]
    "{{20,111},{111}}",	#[111, 20]
    "{{123}}",	#[123]
    "{{4,2,3},{3},{2,3,4,1},{2,3}}"	#[3, 2, 4, 1]
]

for input in inputs:
    print(solution(input))