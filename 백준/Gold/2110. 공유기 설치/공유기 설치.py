import sys

n, c = map(int,sys.stdin.readline().split())
house = []
for i in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()
start = 1
end = house[-1] - house[0]

ans = 0
while start<=end:
    mid = (end+start)//2
    cnt = 1
    cur = house[0]
    for h in house[1::]:
        if h >= cur +mid:
            cnt +=1
            cur = h
    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid -1

print(ans)