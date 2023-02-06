import sys

from collections import Counter



N, M = map(int, input().split())
N_name = [sys.stdin.readline().strip() for i in range(N)]
M_name = [sys.stdin.readline().strip() for i in range(M)]

names = M_name + N_name
after_names = set(names)
result = Counter(names) - Counter(after_names)
lst = (list(result.keys()))
lst.sort()

print(len(lst))
print(*lst, sep ='\n')