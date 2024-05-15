def tower_breakers (t:int):

    n,m = [int(x) for x in input().split()]

    
    if m == 1 or n% 2 == 0:
        print(2)
    else:
        print(1)

