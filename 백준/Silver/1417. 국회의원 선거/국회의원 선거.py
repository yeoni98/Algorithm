import sys

n = int(sys.stdin.readline())
candidate = []
for i in range(n):
    candidate.append(int(sys.stdin.readline()))

candidate2 = sorted(candidate[1:], reverse=True)
ans = 0

while n>1 and candidate[0] <= max(candidate2):
    candidate[0] +=1
    candidate2[0] -=1
    candidate2.sort(reverse=True)
    ans +=1


print(ans)
