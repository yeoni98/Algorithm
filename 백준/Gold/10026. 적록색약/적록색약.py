import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
drawing = []
visited = [[False]*n for i in range(n)]
arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    drawing.append(list(sys.stdin.readline().rstrip()))


def dfs(x,y):
    visited[x][y] = True
    color = drawing[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y +dy[i]

        if 0<=nx<n and 0<=ny<n and drawing[nx][ny] == color and visited[nx][ny] == False:
            dfs(nx,ny)

three_color = 0
two_color = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            three_color +=1


# G -> R로 바꿔서 구간 나누기
for i in range(n):
    for j in range(n):
        if drawing[i][j] == 'G':
            drawing[i][j] = 'R'
visited = [[False]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            two_color += 1

print(three_color, two_color)