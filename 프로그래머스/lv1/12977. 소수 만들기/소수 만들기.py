import math
from itertools import combinations

def prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True
        
def solution(nums):
    ans = 0
    for x in combinations(nums,3):
        if prime_number(sum(x)):
            ans+=1
    
    return ans

# from itertools import combinations
# import math

# def is_prime_number(x):
#     #2부터 x의 제곱근까지의 모든 수를 확인하며
#     for i in range(2, int(math.sqrt(x))+1):
#         #x가 해당 수로 나누어 떨어진다면
#         if x % i == 0:
#             return False # 소수가 아님
#     return True # 소수임

# def solution(nums):
#     answer = 0
#     for x in combinations(nums, 3):
#         if is_prime_number(sum(x)):
#             answer += 1

#     return answer