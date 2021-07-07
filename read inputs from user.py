# Read 2 Matrix Inputs from user
def string_to_list(row):
    matrix=[]
    for i in range(row):
        user_input=list(map(int,input().split()))
        matrix.append(user_input)
    return matrix
    
row,col=map(int,input().split()) #3 3
# NOTE(Telugu):- ENNI MATRIX KAVALO ANNI SARLU FUNCTION NI CALL CHEYAMDI
list1=string_to_list(row)
list2=string_to_list(row)
print(list1)    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list2)    # [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

#INPUT FORMAT
3 3
1 2 3 
4 5 6
7 8 9
10 20 30
40 50 60
70 80 90