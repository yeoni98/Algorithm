import sys

n, p, q = map(int, sys.stdin.readline().split())

dict = {}
dict[0] = 1

def seq(n):
    if n in dict:
        return dict[n]
    else:
        dict[n] = seq(n//p) + seq(n//q)
        return dict[n]


print(seq(n))



