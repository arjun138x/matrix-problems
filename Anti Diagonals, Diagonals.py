def string_to_list(row):
    matrix=[]
    for i in range(row):
        user_input=list(map(int,input().split()))
        matrix.append(user_input)
    return matrix
    
row,col=map(int,input().split()) #3 3
list1=string_to_list(row)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for k in range(row+col-1):
    result=[]
    for i in range(row):
        for j in range(col):
            if k == i+j :
                result.append(list1[i][j])
    print(*result) # print(*result[::-1]) FOR DIAGONALS

#INPUT FORMAT
# 3 3
# 1 2 3 
# 4 5 6
# 7 8 9