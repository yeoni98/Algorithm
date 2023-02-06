import sys
input = sys.stdin.readline

while True:
    ss = input()
    if not ss:
        break
    s, t = ss.split()
    cnt = 0
    flag = 0
    for i in range(len(t)):
        if t[i] == s[cnt]:
            cnt +=1

            if cnt == len(s):
                flag = 1
                break

    if flag == 1:
        print('Yes')
    else:
        print('No')