def string_to_list(row):
    final_list=[]
    for i in range(row):
        user_input=list(map(int,input().split()))
        final_list.append(user_input)
    return final_list
    
row,col=map(int,input().split()) #3 3
rotations=int(input())
rotations//=90
list1=string_to_list(row)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix=list1
for k in range(rotations):
    temp=[]
    for i in range(row):
        # i=col-1-i # COUNTER CLOCK WISE DIRECTION
        result=[]
        for j in range(col):
            j=col-1-j # CLOCK WISE DIRECTION
            result.append(matrix[j][i])
        temp.append(result)
    matrix=temp
for i in matrix:
    print(*i)

#INPUT FORMAT
# 3 3
# 180
# 1 2 3 
# 4 5 6
# 7 8 9