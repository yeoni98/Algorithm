import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))

cnt = 1
while cnt<=m:
    cards.sort()
    s = cards[0]+cards[1]
    cards[0], cards[1] = s,s
    cnt +=1

print(sum(cards))

