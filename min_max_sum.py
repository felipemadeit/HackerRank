def min_max_sum (nums: list):
    
    min_list = nums.copy()
    max_list = nums.copy()
    
    min_array = []
    
    while len(min_array) < 4:
        min_moment = min(min_list)
        min_array.append(min_moment)
        min_list.remove(min_moment)
    
    
    print(min_array)
    
    max_array = []
    
    while len(max_array) < 4:
        max_moment = max(max_list)
        max_array.append(max_moment)
        max_list.remove(max_moment)
    
    print(f"{sum(min_array)} {sum(max_array)}")
    
min_max_sum([1,3,5,7,9])


def min_max_sum_optimization (nums:list):
    
    min_list = nums.copy()
    max_list = nums.copy()
    
    min_num = min(min_list)
    min_list.remove(min_num)
    
    max_num = max(max_list)
    max_list.remove(max_num)
    
    # To find the min i need to remove the max num
    # To finf the max i need to remove the min num
    
    print(f"{sum(max_list)} {sum(min_list)}")
    
min_max_sum_optimization([1,3,5,7,9])