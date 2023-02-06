import re

p = re.compile('^[A-F]?A+F+C+[A-F]?$') #re.compile 로 패턴 저장
for i in range(int(input())):
    print('Good' if p.match(input())==None else 'Infected!') #match() => 처음부터 패턴 일치 여부 확인, 일치 x = None 반환
