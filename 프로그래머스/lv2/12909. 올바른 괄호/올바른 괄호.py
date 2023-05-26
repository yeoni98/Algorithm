from collections import deque
def solution(s):
    q =  deque()
    
    q.append(s[0])
    
    for i in s[1:]:
        if i == "(":
            q.append(i)
        elif i == ")":
            if not q:
                return False
            q.pop()

    if q:
        answer = False
    else:
        answer = True

    return answer
    