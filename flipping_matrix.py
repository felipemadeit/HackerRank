def flip_matrix (matrix:list):
    
    max_sum = 0
    
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            mini_matrix = []
            mini_matrix.append(matrix[i][j])
            mini_matrix.append(matrix[i][len(matrix)-1 -j])
            mini_matrix.append(matrix[len(matrix)-1-i][len(matrix)-1 -j])
            mini_matrix.append(matrix[len(matrix)-1-i][len(matrix)-1 -j])  
            
            max_sum += max(mini_matrix)  
    return max_sum
    
matrix = [[1,2,3,4], [4,5,6,7], [9,8,7,6], [4,7,89,6]]

flip_matrix(matrix)