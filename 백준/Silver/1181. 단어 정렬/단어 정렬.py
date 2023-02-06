import sys
from sys import stdin

n = int(sys.stdin.readline())

word = [sys.stdin.readline().strip() for i in range(n)]
word = set(word)
word = list(word)
word.sort()
word.sort(key=len)

print(*word, sep ='\n')