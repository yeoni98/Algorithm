def solution(phone_book):
    phone_book.sort()
    #["119", "97674223", "1195524421"] -> "119", "1195~", "976~"
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
            return False
            break
    return True

