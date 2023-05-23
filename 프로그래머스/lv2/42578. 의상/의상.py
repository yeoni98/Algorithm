def solution(clothes):
    
    clothes_type = {}

    for v, k in clothes:
        clothes_type[k] = clothes_type.get(k,1) +1
        
    cnt =1
    for v in clothes_type.values():
        cnt*=v
    
    return cnt -1

