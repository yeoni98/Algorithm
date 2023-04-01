r = list(input())
answer = 0
stack = []

for i in range(len(r)):
    if r[i] == '(': #스택 쌓기
        stack.append('(')
        
    else:
        if r[i-1] == '(':
            stack.pop()
            answer += len(stack)
            
        else:
            stack.pop() 
            answer += 1 

print(answer)