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
    answer = set()  # 중복 제거를 위해 집합(set) 사용

    for i in range(1, len(numbers) + 1):
        perm = permutations(numbers, i)
        for p in perm:
            num = int(''.join(p))
            if is_prime(num):
                answer.add(num)

    # 끝이 0인 경우 제외
    for num in answer.copy():  # 복사본을 사용하여 집합을 반복하면서 수정
        if num != 0 and num % 10 == 0:
            answer.remove(num)

    return len(answer)