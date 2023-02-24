import sys

n = int(sys.stdin.readline())
score_list = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    m = a.pop(0)
    a.sort(reverse=True)
    max_gap = a[0] - a[1]
    for j in range(1,m-1):
        if max_gap < a[j] - a[j+1]:
            max_gap = a[j]-a[j+1]
    print('Class',i+1)
    print('Max',str(max(a))+',', 'Min',str(min(a))+',', 'Largest gap',max_gap)