import sys
s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())
ans = 0
def dfs(T):
    if s == T:
        print(1)
        exit()

    if len(T) == 0:
        return 0

    if T[-1] == 'A':
        dfs(T[:-1])
    if T[0] == 'B':
        dfs(T[1:][::-1])


if dfs(t):
    print(1)
else:
    print(0)
