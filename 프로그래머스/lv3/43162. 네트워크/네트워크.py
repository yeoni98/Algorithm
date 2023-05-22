def solution(n, computers):
    cnt = 0
    visit = [0]*n
    
    def dfs(i):
        visit[i] = 1
        for a in range(n):
            if computers[i][a] != 0 and visit[a]==0:
                dfs(a)
                
    for i in range(n):
        if visit[i] == 0:
            dfs(i)
            cnt +=1
    return cnt