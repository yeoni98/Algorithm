from itertools import permutations
import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    lst = []
    for i in range(1, len(numbers) + 1):
        p = permutations(numbers, i)
        for j in p:
            num = int(''.join(j))
            if is_prime(num) and num not in lst:
                lst.append(num)

    return len(lst)
