import sys

s = list(sys.stdin.readline().rstrip())
i = 0
j = 0

while i < len(s):
    if s[i] == '<':            #< > 의 경우
        i +=1
        while s[i] != '>':
            i +=1
        i +=1
    elif s[i].isalnum():          #알파벳, 숫자의 경우
        j = i
        while i < len(s) and s[i].isalnum():
            i +=1
        word = s[j:i]
        word.reverse()
        s[j:i] = word

    else:                           # 괄호
        i+=1

print(''.join(s))