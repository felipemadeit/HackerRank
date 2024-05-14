def diagonladifference (nums: list):
    
    first_diagon = []
    second_diagon = []
    
    
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if i == j:
                first_diagon += nums[i][j]
                
    new_list = list(reversed(nums))
    

    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            if i == j:
                second_diagon += new_list[i][j]
  
    print(abs(second_diagon-first_diagon))
    

n = int(input())
arr = []

for i in range(n):
    line = [int(x) for x in input().split()]
    arr.append(line)
    
diagonladifference(arr)