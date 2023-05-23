def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
            return False
            break
    return True

# 길이가 가장 짧은  min - len(min) 으로 다른 것[:len(min)]이 같은가
# 만약 같은 자리 수의 숫자일 땐 ..? 어떻게 판별..?
