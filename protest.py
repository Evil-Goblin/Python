

board = [[1,1,4,3],[3,2,1,4],[3,1,4,2],[2,1,3,3]]

b_set = []

answer = 0


b_len = len(board)
b_rng = range(len(board))
for x in b_rng:
    for y in b_rng:

        temp = board[x][y]
        ### 11x
        if y+2 < b_len:
            
            if temp == board[x][y+1] :
                if y+3 < b_len:
                    if temp == board[x][y+3] :
                        b_set.append([x,y+3,x,y+2])

                        # answer += 1
                        # print(x,y)
                if x-1 > 0 :
                    if temp == board[x-1][y+2]:

                        b_set.append([x-1,y+2,x,y+2])
                        # answer += 1
                        # print(x,y)
                if x+1 < b_len :
                    if temp == board[x+1][y+2]:
                        b_set.append([x+1,y+2,x,y+2])
                        # answer += 1
                        # print(x,y)

            if temp == board[x][y+2]:
                if x-1 > 0 :
                    if temp == board[x-1][y+1]:
                        b_set.append([x-1,y+1,x,y+1])
                        # answer += 1
                        # print(x,y)
                elif x+1 < b_len :
                    if temp == board[x+1][y+1]:
                        b_set.append([x+1,y+1,x,y+1])
                        # answer += 1
                        # print(x,y)
            if y+3 < b_len:
                if temp == board[x][y+2] and temp == board[x][y+3] :
                    b_set.append([x,y,x,y+1])



        if x+2 < b_len:
            if temp == board[x+1][y]:
                if y-1 > 0 :
                    if temp == board[x+2][y-1]:
                        b_set.append([x+2,y-1,x+2,y])
                        # answer += 1
                        # print(x,y)
                if y+1 < b_len :
                    if temp == board[x+2][y+1]:
                        b_set.append([x+2,y+1,x+2,y])
                        # answer += 1
                        # print(x,y)
                if x+3 < b_len :
                    if temp == board[x+3][y]:
                        b_set.append([x+3,y,x+2,y])
                        # answer += 1
                        # print(x,y)
            if temp == board[x+2][y]:
                if y-1 > 0 :
                    if temp == board[x+1][y-1] :
                        b_set.append([x+1,y-1,x+1,y])
                        # answer += 1
                        # print(x,y)
                if y+1 < b_len :
                    if temp == board[x+1][y+1] :
                        b_set.append([x+1,y+1,x+1,y])
                        # answer += 1
                        # print(x,y)

            if x+3 < b_len:
                if temp == board[x+2][y] and temp == board[x+3][y] :
                    b_set.append([x,y,x+1,y])

        ### 1 x 1

        #if 
a_set = []

for i in b_set :
    tr = True
    for j in a_set:
        if i == j :
            tr = False
            break
    if tr :
        a_set.append(i)
        
if len(a_set) > 0 :
        answer = len(a_set)
    else :
        answer = -1

# print(answer)