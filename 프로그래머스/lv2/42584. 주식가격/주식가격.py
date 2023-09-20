def solution(prices):
    result = []
    for i in range(len(prices)):
        time = 0
        for j in range(i+1,len(prices)):
            if prices[j]<prices[i]:
                time = j-i
                break
            if j == len(prices)-1:
                time = j-i
        result.append(time)
                
    
    return result
                