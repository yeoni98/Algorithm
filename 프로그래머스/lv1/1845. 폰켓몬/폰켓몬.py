def solution(nums):
    n = len(nums)
    a = len(set(nums))
    b = n // 2
 
    answer = 0
        
    if a < b:
        answer = a
    else:
        answer = b
        
    return answer

   


