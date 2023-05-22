def solution(numbers, target):
    leaves = [0]
    cnt = 0
    
    for num in numbers:
        temp = []
        
        for leaf in leaves:
            temp.append(leaf+num)
            temp.append(leaf-num)
        
        leaves = temp
        
    for leaf in leaves:
        if leaf == target:
            cnt +=1
    
    
    
    
    return cnt