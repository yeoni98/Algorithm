import sys

n = int(sys.stdin.readline())
request = list(map(int,sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

start = 0
end = max(request)
ans = 0

while start<=end:
    total = 0
    mid = (end+start)//2
    for r in request:
        if r>mid:
            total += mid
        else:
            total +=r
        if total>budget:
            break
    if total == budget:
        ans = mid
        break
    if total<budget:
        ans = mid
        start = mid +1

    else:
        end = mid-1


print(ans)