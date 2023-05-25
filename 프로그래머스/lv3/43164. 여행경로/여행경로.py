from collections import deque

def solution(tickets):
    answer = []
    path = {}
    
    for (start, end) in tickets:
        if start in path:
            path[start].append(end)
        else:
            path[start] = [end]
            
    for p in path.keys():
        path[p].sort(reverse = True)
    
    st = ["ICN"]
    
    while st:
        top = st[-1]
        if (top not in path) or (not path[top]):
            answer.append(st.pop())
            
        else:
            st.append(path[top].pop())
    
    
    
    return answer[::-1]