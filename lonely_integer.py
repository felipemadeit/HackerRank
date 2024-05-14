def lonelyinteger (nums:list):
    
    ocurrences = {}
    
    sorted_nums = sorted(nums)
    for num in sorted_nums:
        if num in ocurrences:
            ocurrences[num] += 1
        else:
            ocurrences[num] = 1

    for key,values in ocurrences.items():
        if values == 1:
            print(key)
        
    
        
    
        

lonelyinteger([0,0,1,2,1])