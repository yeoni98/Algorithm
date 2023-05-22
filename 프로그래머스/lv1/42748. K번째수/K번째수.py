def solution(array, commands):
    answer = []
    for c in commands:
        s = array[int(c[0])-1:c[1]]
        s.sort()
        answer.append(s[int(c[2])-1])
        
    return answer