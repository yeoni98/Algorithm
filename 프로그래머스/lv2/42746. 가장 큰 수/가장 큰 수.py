def solution(numbers):
    l = list(map(str, numbers))
    l.sort(key = lambda x:x*3, reverse = True)
    answer = int(''.join(l))
    return str(answer)

