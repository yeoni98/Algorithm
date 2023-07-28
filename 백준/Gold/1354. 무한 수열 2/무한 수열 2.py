# import sys
# 
# n, p, q, x, y = map(int,sys.stdin.readline().split())
# 
# dict = {}
# dict[0] = 1
# 
# def seq(n):
#     if n in dict:
#         return dict[n]
#     else:
# 
#         dict[n] = seq(n//p-x) + seq(n//q-y)
#         return dict[n]
# 
# 
# print(seq(n))



import sys

n, p, q, x, y = map(int,sys.stdin.readline().split())

dict = {}
dict[0] = 1

def seq(n):
    if n in dict:
        return dict[n]
    else:
        if (n//p)-x <=0:
            n1 = 0
        else:
            n1 = (n//p)-x
        if (n//q)-y <=0:
            n2 = 0
        else:
            n2 = (n//q)-y
        dict[n] = seq(n1) + seq(n2)
        return dict[n]



print(seq(n))







