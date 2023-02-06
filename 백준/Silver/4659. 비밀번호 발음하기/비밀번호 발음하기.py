vow = ['a','e','i','o','u']

accept = ['ee','oo']

while True:
    cnt = 0
    pswd = input()
    x = y = 0
    if pswd == 'end':
        break
    for i in vow:
        if i in pswd:
            cnt +=1
    if cnt < 1:
        print('<%s> is not acceptable.' %pswd)
        continue

    for i in range(len(pswd)-2):
        if pswd[i] in vow and pswd[i+1] in vow and pswd[i+2] in vow:
            x = 1
        elif not(pswd[i] in vow) and not(pswd[i+1] in vow) and not(pswd[i+2] in vow):
            x = 1
    if x == 1:
        print('<%s> is not acceptable.' % pswd)
        continue
    for i in range(len(pswd)-1):
        if pswd[i] == pswd[i+1]:
            if pswd[i] =='e' or pswd[i] =='o':
                continue
            else:
                y = 1
    if y == 1:
        print('<%s> is not acceptable.' %pswd)
        continue
    else:
        print('<%s> is acceptable.' %pswd)