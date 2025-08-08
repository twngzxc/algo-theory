t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    grid = list(input())
 
    # if no walls or at the ends
    if "#" not in grid or x == 1 or x == n:
        print(1)
        continue
 
    else:
        
        leftwall = -1
        rightwall = -1
        
        for i in range(x-1, -1, -1):
            if grid[i] == "#":
                leftwall = i+1
                break
        
        for i in range(x-1, n, 1):
            if grid[i] == "#":
                rightwall = i+1
                break
        
        if leftwall == -1:
            # mani must put left, so i go right
            right_distance = n-rightwall+2
            left_distance = x
            if right_distance > left_distance:
                print(left_distance) # i will still go left
                continue
            else:
                print(right_distance)
                continue
                
        if rightwall == -1:
            # mani must put right, so i go left
            right_distance = n-x+1
            left_distance = leftwall+1
            if right_distance < left_distance:
                print(right_distance) # i will still go right
                continue
            else:
                print(left_distance)
                continue
        
        
        right_distance = n - rightwall + 2 #if mani put on left
        left_distance = leftwall + 1   # if mani put on right
        
        if right_distance < left_distance:
            #mani will put on right, so i will go left
            #if i insist on going right
            if left_distance > n-x+1:  #i will still go right cos right is shorter
                print(n-x+1)
                continue
            else:
                print(left_distance)
                continue
            
        if left_distance < right_distance:
            # mani will put on left, so i will go right
            # if i insist on going left
            if right_distance > x:
                print(x)
                continue
            else:
                print(right_distance)
                continue
            
        if left_distance == right_distance:
            print(right_distance)
            continue
