import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, d = map(int,sys.stdin.readline().split())
    matrix = []
    for _ in range(n):
        row = list(map(int,sys.stdin.readline().split()))
        matrix.append(row)
    if d<0:
        d +=360

    rotation = d//45

    for _ in range(rotation):
        origin = []

        #주 대각선
        for j in range(n):
            origin.append(matrix[j][j])

        #주 대각선 -> 수직선
        for j in range(n):
            temp = matrix[j][n//2]
            matrix[j][n//2] = origin[j]
            origin[j] = temp

        #수직선 -> 부 대각선
        for j in range(n):
            temp = matrix[j][n-j-1]
            matrix[j][n-j-1] = origin[j]
            origin[j] = temp

        #부 대각선 -> 수평선
        for j in range(n):
            temp = matrix[n//2][n-j-1]
            matrix[n//2][n-j-1] = origin[j]
            origin[j] = temp

        #수평선 -> 주 대각선
        for j in range(n):
            matrix[n-j-1][n-j-1] = origin[j]
    for m in matrix:
        print(*m)

