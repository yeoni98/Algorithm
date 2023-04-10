def solution(s):

    q = deque()
    q.append(s[0])
    for i in range(1,len(s)):
        if s[i] == ')':
            if len(q) != 0 :
                q.pop()
            else: 
                answer = False
                    
        if s[i] == '(':
            q.append(s[i])
    if len(q)>0:
        answer = False
    else:
        answer = True
    

    return answer


from collections import deque