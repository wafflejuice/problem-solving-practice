def solution(msg):
    dic = {}
    for i in range(26):
        dic = add_to_dic(dic, chr(ord('A')+i))
    
    print_idxs = []
    while len(msg) > 0:
        dic, msg, print_idx = consume(dic, msg)
        print_idxs.append(print_idx)
    answer = print_idxs
    return answer

def add_to_dic(dic, word):
    dic[word] = len(dic.keys())+1
    return dic

def consume(dic, msg):
    print_idx = -1
    for mi in range(1, len(msg)+1):
        # print(f'prepare to consume {msg[:mi - 1]}, from {msg}')
        if msg[:mi] in dic.keys() and mi+1 < len(msg)+1:
            continue
        elif msg[:mi] in dic.keys() and mi+1 == len(msg)+1:
            print_idx = dic[msg[:mi]]
            return dic, '', print_idx
        else:
            print_idx = dic[msg[:mi-1]]
            dic = add_to_dic(dic, msg[:mi])

            # print(f'consume {msg[:mi-1]} aka {dic[msg[:mi-1]]}, remains {msg[mi-1:]}')
            # print(f'dic = {dic}')
            
            return dic, msg[mi-1:], print_idx

sample_inputs = ['KAKAO', 'TOBEORNOTTOBEORTOBEORNOT', 'ABABABABABABABAB']
for s in sample_inputs:
    print(solution(s))

# 약 31분