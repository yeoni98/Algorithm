import math

def totalMinutes(time):
    h,m = map(int, time.split(':'))
    return h*60+m

def solution(fees, records):
    answer =[]
    dic = dict()
    
    t, f, pt, pf = fees
    for l in records:
        time, number, order = l.split(" ")
        number = int(number)
        if number in dic:
            dic[number].append([totalMinutes(time), order])
        else:
            dic[number] = [[totalMinutes(time), order]]
        
    lst = list(dic.items())
    lst.sort(key=lambda x: x[0])

    
    for l in lst:
        tt = 0
        
        for ll in l[1]:
            if ll[1] == "IN":
                tt -= ll[0]
                print(tt)
            else:
                tt += ll[0]
            
        
        if l[1][-1][1] == "IN":
            tt += totalMinutes('23:59')
        if tt <= t:
            answer.append(f)
        else:
            answer.append(f+math.ceil((tt-t)/pt)*pf)
                
    return answer

# 차량번호, 시간, in/out 으로 다시 리스트 만들기
# 차량번호 올림차순으로 정렬 => 입차 출차 계산
