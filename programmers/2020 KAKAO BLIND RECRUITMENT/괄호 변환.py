def solution(p):
    if p=='':
        return ''

    h=0
    i=0
    while i<len(p):
        if i>0 and h==0:
            break

        if p[i]=='(':
            h+=1
        else:
            h-=1
        i+=1

    stack=[]
    is_correct=True
    j=0
    while j<i:
        if p[j]=='(':
            stack.append('(')
        else:
            if len(stack)>0:
                stack.pop()
            else:
                is_correct=False
                break
        j+=1

    if is_correct:
        return p[:i]+solution(p[i:])

    front='('+solution(p[i:])+')'
    back=p[:i][1:-1].replace(')', 't').replace('(', ')').replace('t', '(')

    return front+back

print(solution("(()())()")) # "(()())()"
print(solution(")(")) # "()"
print(solution("()))((()")) # "()(())()"
