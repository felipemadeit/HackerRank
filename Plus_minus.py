def plus_minus(arr):
    positive = 0
    negative = 0
    zerooos = 0
    
    for nums in arr:
        if nums > 0:
            positive += 1
        elif nums < 0:
            negative += 1
        else:
            zerooos += 1
    
    print(positive/len(arr))
    print(negative/len(arr))
    print(zerooos/len(arr))
    
plus_minus(arr = [1,1,0,-1,-1])