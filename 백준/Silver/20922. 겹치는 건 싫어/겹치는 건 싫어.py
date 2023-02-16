import sys

n,k = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))

len = 0
left, right = 0,0
counter = [0]*(max(num)+1)
ans = 0

while right<n:
    if counter[num[right]] < k:
        counter[num[right]] += 1
        right += 1
    else:
        counter[num[left]] -= 1
        left += 1
    ans = max(ans, right - left)
print(ans)