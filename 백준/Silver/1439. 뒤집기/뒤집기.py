
import sys

m = list(sys.stdin.readline().rstrip())

cnt = 0
for i in range(len(m)-1):
    if m[i] == m[i+1]:
        continue
    else:
        cnt +=1
if cnt == 0:
    print('0')
elif cnt == 1:
    print('1')
elif cnt %2 == 0:
    print(int(cnt/2))
elif cnt%2 !=0:
    print(int(cnt/2)+1)