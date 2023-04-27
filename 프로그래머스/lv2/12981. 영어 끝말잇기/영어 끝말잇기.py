from collections import deque

def solution(n, words):
    
    x, y = 0,0
    used = []
    used.append(words[0])
    last = words[0][-1]
    for i in range(1,len(words)):
        if words[i] not in used and words[i][0] == last:
            used.append(words[i])
            last = words[i][-1]
        else:
            x = (i%n)+1
            y = (i//n)+1
            break
    return[x,y]
