def solution(genres, plays):
    answer = []
    
    dict1 = {}
    dict2 = {}
    for i, (k, v) in enumerate(zip(genres, plays)):
        if k not in dict1:
            dict1[k] = [(i,v)]
        else:
            dict1[k].append((i,v))
        if k not in dict2:
            dict2[k] = v
        else:
            dict2[k] += v
            
    for k, v in sorted(dict2.items(), key = lambda x:x[1], reverse = True):
        for i, value in sorted(dict1[k], key = lambda x:x[1], reverse = True)[:2]:
            answer.append(i)
    
    
    return answer
# 1. dict1 에 k에 따른 (i, v) 저장 len(dict1[k]) 로 나열~
# 2. dict2[i] = v. i에 대한 v 저장 => 내부에서 v를 내림차순으로 -> 2개만
# 3. 
# 4. cnt 2
# dict 로 key 별로 +1 하기, 
# dict.value.sort(reverse = True)
# 고유 번호 순서 => Dict 로..?
# 두개씩이니까 확인해야..
                  

