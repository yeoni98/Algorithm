import sys

n, x = map(int,sys.stdin.readline().split())

num = list(map(int,sys.stdin.readline().split()))
result = []
if max(num) == 0:
    print("SAD")
else:
    value = sum(num[:x])
    max_value = value
    max_cnt = 1
    for i in range(x,n):
        value += num[i]
        value -= num[i-x]

        if value>max_value:
            max_value = value
            max_cnt = 1

        elif value == max_value:
            max_cnt += 1
        

    print((max_value),max_cnt,sep='\n')
