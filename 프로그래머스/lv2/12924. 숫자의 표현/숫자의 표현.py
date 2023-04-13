def solution(n):
    ans = 0
    
    for i in range(1,n+1):
        sums = 0
        for j in range(i, n+1):
            sums += j
            if sums == n:
                ans +=1
            if sums>n:
                break;
    return ans