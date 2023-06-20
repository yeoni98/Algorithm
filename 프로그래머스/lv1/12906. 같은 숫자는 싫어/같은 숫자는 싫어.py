def solution(arr):
    rst = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            rst.append(arr[i])
    rst.append(arr[-1])
        
    return rst