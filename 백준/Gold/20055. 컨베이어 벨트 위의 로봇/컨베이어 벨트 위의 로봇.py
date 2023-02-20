import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
belt = deque(list(map(int,sys.stdin.readline().split())))
robot = deque([0]*n)
cnt = 0

while 1:
    #1단계
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 로봇이 내려가는 곳이라서

    if sum(robot):
        #2단계
        for i in range(n-2,-1,-1): # i에 이동하려는 로봇이 있고 이동하려는 i+1 자리에 로봇이 없어야 되고, belt 는 0보다 1이상이어야 함.
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
        robot[-1] = 0
        
    # 3단계
    if belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1
    cnt += 1
    #4단계
    if belt.count(0) >= k:
        break
print(cnt)