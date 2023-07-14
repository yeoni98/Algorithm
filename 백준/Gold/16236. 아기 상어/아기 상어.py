import sys

n = int(sys.stdin.readline())

space = []
shark = []
shark_size = 2
eat_cnt = 0
time = 0
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if l[j] == 9:
            shark = [i, j]
            l[j] = 0
    space.append(l)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global eat_cnt, time, shark_size, shark
    visited = [[False] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = True
    queue = [(shark[0], shark[1], 0)]
    edible_fish = []
    while queue:
        x, y, t = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if space[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    queue.append((nx, ny, t + 1))
                    if 0 < space[nx][ny] < shark_size:
                        edible_fish.append((t + 1, nx, ny))
    if not edible_fish:
        return False
    edible_fish.sort()
    t, x, y = edible_fish[0]
    time += t
    space[x][y] = 0
    shark = [x, y]
    eat_cnt += 1
    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0
    return True


while bfs():
    pass

print(time)
