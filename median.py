

def findMedian(arr):
    # Write your code here
    
    _len = len(arr)
    _sorted = sorted(arr)
    
    if _len %2 != 0:
        middle = _len//2
        print(_sorted[middle])
    else:
        middle = arr[_len//2-1] + arr[_len//2]
        print(middle)
        
findMedian([1,2,3,4,5,6])