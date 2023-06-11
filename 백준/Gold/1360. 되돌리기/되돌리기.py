import sys

n = int(sys.stdin.readline())

l = []
text = ''

for i in range(n):

    ord, txt, sec = sys.stdin.readline().split()
    l.append((ord,txt,int(sec)))

state = [('type', '', 0)]

for s in l:
    if s[0] == 'type':
        text += s[1]
        state.append((s[0],text,s[2]))


    else:
        for i in range(len(state)-1,-1,-1):
            if state[i][2]< s[2] - int(s[1]):
                text = state[i][1]
                break
        if s[2] - int(s[1]) <= 0:
            text = ''

        state.append((s[0],text,s[2]))

print(text)