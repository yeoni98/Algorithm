from itertools import permutations
import sys

babbling = list(sys.stdin.readline().split())
print(babbling)
def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    lst = []
    for i in range(1, len(words) + 1):
        for j in permutations(words, i):
            lst.append(''.join(j))
            print(lst)

    for i in babbling:
        if i in lst:
            answer += 1
    return answer

print(solution(babbling))