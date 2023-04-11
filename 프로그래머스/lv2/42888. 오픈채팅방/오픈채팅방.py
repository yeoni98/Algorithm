def solution(record):
    answer = []
    orders = []
    userDB = dict()
    
    for i in record:
        info = i.split(" ")
        order, userId = info[0], info[1]
        if order in ("Enter", "Change"):
            nickname = info[2]
            userDB[userId] = nickname
        orders.append((order, userId))
    
    for i in orders:
        order, userId = i[0], i[1]
        if order == 'Enter':
            answer.append(f'{userDB[userId]}님이 들어왔습니다.')
        if order == 'Leave':
            answer.append(f'{userDB[userId]}님이 나갔습니다.')
            
    return answer
