def recursive_sum (x: int):
    
    list_x = list(map(int, str(x)))


    super_digit = 0
    


    for nums in list_x:
        super_digit += nums
    print(super_digit)

recursive_sum(int(input()))