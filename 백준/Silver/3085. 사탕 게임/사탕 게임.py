import sys

n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline()) for i in range(n) ]
ans = 0

def check(arr):
    n = len(arr)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt>ans:
                ans = cnt
        cnt = 1
        for j in range(1,n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt =1
            if cnt > ans:
                ans = cnt

    return ans

for i in range(n):
    for j in range(n):
        if j+1<n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp = check(arr)
            if temp > ans:
                ans = temp
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i+1<n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            temp = check(arr)
            if temp>ans:
                ans = temp
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(ans)
