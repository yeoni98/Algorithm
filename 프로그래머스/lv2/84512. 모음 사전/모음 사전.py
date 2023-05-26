from itertools import product

def solution(word):
    l = []
    for i in range(1, 6):
        for j in product('AEIOU', repeat=i):
            l.append(''.join(list(j)))
    l.sort()
    
    return l.index(word)+1
        