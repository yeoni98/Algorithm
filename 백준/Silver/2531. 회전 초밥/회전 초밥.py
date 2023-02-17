import sys

n, d, k, c = map(int,sys.stdin.readline().split())
sushi = []


for i in range(n):
    sushi.append(int(sys.stdin.readline()))
sushi = sushi*2

def maximum(t):
    cnt = 0

    for i in range(n):
        eaten = sushi[i:i+k]
        eaten.append(c)
        kinds = len(set(eaten))
        if kinds > cnt:
            cnt = kinds

    return cnt

print(maximum(sushi))
#15961과 비교
