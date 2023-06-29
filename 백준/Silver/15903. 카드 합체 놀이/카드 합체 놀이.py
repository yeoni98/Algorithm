import sys
import heapq
from heapq import heapify

n, m = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
heapify(cards)

for i in range(m):
    hap = heapq.heappop(cards) + heapq.heappop(cards)
    for j in range(2):
        heapq.heappush(cards, hap)

print(sum(cards))

