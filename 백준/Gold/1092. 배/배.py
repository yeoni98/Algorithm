import sys

n = int(sys.stdin.readline())
crane = list(map(int,input().split(' ')))
m = int(sys.stdin.readline())
boxes = list(map(int,input().split(' ')))

boxes.sort(reverse=True)
crane.sort(reverse=True)

if max(crane) < max(boxes):
    print(-1)
    sys.exit()

positions = [0]*n

checked = [0]*m

result = 0
cnt = 0

while True:
    if cnt == len(boxes):
        break
    for i in range(n):
        while positions[i] < len(boxes):
            if checked[positions[i]] == 0 and crane[i] >= boxes[positions[i]]:
                checked[positions[i]] = 1
                positions[i] += 1
                cnt +=1
                break
            positions[i] += 1
    result +=1

print(result)


