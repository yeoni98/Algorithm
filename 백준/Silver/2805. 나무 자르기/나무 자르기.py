import sys

n ,m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(trees)
ans = 0
while start<=end:
    total = 0
    mid = (end+start)//2
    for t in trees:
        if t>mid:
            total += (t-mid)
        if total>m:
            break
    if total<m:
        end = mid -1
    else:
        start = mid+1
        ans = mid

print(ans)