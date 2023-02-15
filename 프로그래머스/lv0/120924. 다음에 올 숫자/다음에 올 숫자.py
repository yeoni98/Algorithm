def solution(common):
    answer = 0
    if common[1]-common[0] == common[2]-common[1]:
        answer = common[-1] + (common[1]-common[0])
    else:
        r = common[1]/common[0]
        answer = common[-1]*r
    return answer