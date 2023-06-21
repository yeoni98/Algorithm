
def solution(progresses, speeds):
    day = 0
    cnt = 0
    ans = []
    while len(progresses)>0:
        if progresses[0] + day*speeds[0] >= 100:
            speeds.pop(0)
            progresses.pop(0)
            cnt +=1
        else:
            if cnt>0:
                ans.append(cnt)
                cnt = 0
            day +=1
    ans.append(cnt)
    return ans
    