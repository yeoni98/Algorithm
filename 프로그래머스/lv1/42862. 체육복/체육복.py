
def solution(n, lost, reserve):
    ans = 0 
    lost_after = set(lost) - set(reserve)
    reserve_after = set(reserve) - set(lost)
    
    for i in reserve_after:
        if i-1 in lost_after:
            lost_after.remove(i-1)
        elif i+1 in lost_after:
            lost_after.remove(i+1)
        
    ans = n - len(lost_after)
    
    return ans
    
