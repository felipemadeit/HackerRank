def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2)
    a[mid], a[n-1] = a[n-1], a[mid]
    print(a)


    k = int((n)/2)

    a[k:] = sorted(a[k:], reverse=True)
    

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = [int(x) for x in input().split()]
    findZigZagSequence(a, n)

