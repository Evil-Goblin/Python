def solution(v):
    
    x = []
    y = []
    
    
    
    for i in range(3):
        x.append(v[i][0])
        y.append(v[i][1])

    print(x)
    print(y)
        
    x_set = set(x)
    y_set = set(y)

    print(x_set)
        
    answer = [list(x_set)[0],list(y_set)[0]]

    return answer




v = [[1, 1], [2, 2], [1, 2]]

print(solution(v))

exe