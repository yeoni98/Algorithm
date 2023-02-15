import sys
n = int(sys.stdin.readline())
dl =  []
for i in range(6):
    d, l = list(map(int,sys.stdin.readline().split()))
    dl.append((d,l))
dl2 = dl*2
max1 = []
max2 = []
for i in range(6):
    if dl[i][0] == 2 or dl[i][0] == 1:
        max1.append(dl[i])
idx1 = dl.index(max(max1, key = lambda x : x[1]))


for i in range(6):
    if dl[i][0] == 4 or dl[i][0] == 3:
        max2.append(dl[i])
idx2 = dl.index(max(max2, key = lambda x : x[1]))


idx = 0

if max(idx1,idx2)-min(idx1,idx2) != 1:
    idx = min(idx1,idx2)
else:
    idx = max(idx1,idx2)

ans = n*(dl[idx1][1]*dl[idx2][1] - dl2[idx+2][1]*dl2[idx+3][1])
print(ans)
