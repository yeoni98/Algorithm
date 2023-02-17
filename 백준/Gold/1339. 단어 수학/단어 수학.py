import sys

n = int(sys.stdin.readline())

alphadict = {} # 단어를 저장할 리스트
alpha = [] # 단어를 저장할 리스트
numlist = [] # 수를 저장할 리스트

for i in range(n):
    alpha.append(sys.stdin.readline().rstrip())
for i in range(n):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alphadict: # 단어의 알파벳이 이미 dict에 있으면
            alphadict[alpha[i][j]] += 10**(len(alpha[i])-j-1) # 자리에 맞게 추가 ( 1의 자리면 1 )
        else:
            alphadict[alpha[i][j]] = 10**(len(alpha[i])-j-1)

for value in alphadict.values():# dict에 저장된 수들을 모두 리스트에 추가
    numlist.append(value)

numlist.sort(reverse = True)
sum = 0
pows = 9

for i in numlist:
    sum += i*pows
    pows -= 1

print(sum)
