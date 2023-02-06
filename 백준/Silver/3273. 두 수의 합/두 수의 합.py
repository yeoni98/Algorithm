import sys

n = int(sys.stdin.readline())
a = list(map(int,input().split()))
x = int(input())

result = 0
i = 0
j = n-1
a.sort()


while i<j:
    sum = a[i] + a[j]
    if sum == x:
        result +=1
        i += 1
        j -= 1
    elif sum <x:
        i+=1
    else:
        j -=1
print(result)