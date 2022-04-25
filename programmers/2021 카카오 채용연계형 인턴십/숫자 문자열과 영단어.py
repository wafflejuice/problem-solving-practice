def solution(s):
    num_words=['zero','one','two','three','four','five','six','seven','eight','nine']
    ans=[]
    memory=''
    for si in range(len(s)):
        if s[si] in '0123456789':
            ans.append(s[si])
        else:
            memory += s[si]
            if memory in num_words:
                ans.append(str(num_words.index(memory)))
                memory=''

    return int(''.join(ans))

print(solution("one4seveneight")) # 1478
print(solution("23four5six7")) # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123")) # 123
