import sys
from collections import defaultdict

n, d, k, c = map(int,sys.stdin.readline().split())
sushi = []



for i in range(n):
    sushi.append(int(sys.stdin.readline()))
sushi += sushi[:k-1] # sushi*2라고 했는데 그것보다 sushi 마지막에서 + k-1개만큼만 더 있으면 되니까

left, right, cnt = 0, 0, 0
eat = defaultdict(int)
eat[c] += 1

def maximum(sushi):
    global cnt, right, left

    for right in range(len(sushi)):
        eat[sushi[right]] +=1

        if right >= k-1:
            cnt = max(cnt, len(eat))
            eat[sushi[left]] -= 1
            if eat[sushi[left]] == 0:
                del eat[sushi[left]]
            left +=1
    print(cnt)




maximum(sushi)
