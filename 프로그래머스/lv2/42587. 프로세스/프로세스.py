
from collections import deque

def solution(priorities, location):
    queue = deque((i,j) for i, j in enumerate(priorities))
    ans = []
    
    while queue:
        q = queue.popleft()
        if queue and any(q[1]<qq[1] for qq in queue):
            queue.append(q)
        else:
            ans.append(q)
            
        
    for i in ans:
        if i[0] == location:
            return ans.index(i)+1
            
            
    
#     m = max(priorities)
#     counters = Counter(priorities)
#     if counters[m] != 1:
#         answer = location + 1
#     elif counters[m] == 1:
#         r = alphabet[location]
#         start_index = priorities.index(max(priorities))
#         ans = alphabet[start_index:]+alphabet[:start_index]
#         answer = ans.index(r)+1
    