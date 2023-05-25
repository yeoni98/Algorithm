def solution(number, k):
    stack = [number[0]]
    
    for num in number[1:]:
        while stack and stack[-1]<num and k>0:
            stack.pop()
            k-=1
        stack.append(num)
    
    return "".join(stack) if k==0 else "".join(stack[:len(number)-k])

