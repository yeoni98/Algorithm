import sys
input = sys.stdin.readline

def BFS(graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 1
    queue = set([(0, 0, graph[0][0])])			# set 중복제거, 시간초과 방지
    while queue:
        x, y, visited = queue.pop()
        result = max(result, len(visited))		# 문자열 길이를 통해 이동거리 측정
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not graph[nx][ny] in visited:	# 지나온 모든 알파벳과 다르다면
                    queue.add((nx, ny, visited + graph[nx][ny]))
    return result

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

answer = BFS(board)
print(answer)


