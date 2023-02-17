import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    num = []
    cnt = 0
    if n == 1:
        print('YES')
        continue


    else:
        breaker = False
        for j in range(n):
            num.append(sys.stdin.readline().rstrip())
        num.sort() # 전화번호는 문자열로 인식되어 Ex) 정렬 시 '1234',  '145', '12345' -> '1234', '12345', '145'
        for j in range(n-1):
            # print(num[j], num[j + 1][:len(num[j])])
            # 문자열로 정렬되었으므로 바로 옆만 비교
            if num[j] == num[j+1][:len(num[j])]:
                print("NO")
                breaker = True
                break
        if breaker != True:
            print("YES")