import sys

n = int(sys.stdin.readline())
chess = [0]*n

def check(x):
    for i in range(x):
        if chess[i] == chess[x] or abs(chess[i]-chess[x]) == x-i:
            return False

    return True
ans = 0
def queen(x,n):
    global ans
    if x==n:
        ans +=1
    else:
        for i in range(n):
            chess[x] = i
            if check(x):
                queen(x+1,n)

queen(0,n)
print(ans)