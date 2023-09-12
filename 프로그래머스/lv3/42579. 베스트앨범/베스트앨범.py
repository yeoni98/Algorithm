def solution(genres, plays):
    answer = []
    
    dict1 = {} #장르의 인덱스 값
    dict2 = {} # 각 장르의 총 재생횟수
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        # 0, classic, 500
        # 1, pop, 600
        if g not in dict1:
            dict1[g] = [(i,p)] # dict1[classic] = [(0,500)]
        else:
            dict1[g].append((i,p))
            
        if g not in dict2:
            dict2[g] = p
        else:
            dict2[g] += p
    
    #재생횟수를 기준으로 내림차순으로 정렬
    for k, v in sorted(dict2.items(), key = lambda x:x[1], reverse = True): 
        # 해당 장르(k)의 재생횟수를 기준으로 내림차순 정렬(2개만))
        for i, value in sorted(dict1[k], key = lambda x:x[1], reverse = True)[:2]:
        # dict1['pop'] = [(4, 2500),(1, 600)]
            answer.append(i)
    
    
    return answer

