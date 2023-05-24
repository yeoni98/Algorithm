def solution(sizes):
    
    x_list = []
    y_list = []
    for i in range(len(sizes)):
        x = sizes[i][0]
        y = sizes[i][1]
        if x>y:
            sizes[i][0] = y
            sizes[i][1] = x
    
    for x,y in sizes:
        x_list.append(x)
        y_list.append(y)
        
    return max(x_list)*max(y_list)
        