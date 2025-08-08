num = int(input())
for i in range(num):
    n = int(input())
    a = list(map(int, input().split()))
    if max(a) == -1 and min(a) == -1:
        print("yes")
    elif min(a) > -1:
        mex = max(a) - min(a)
        smallest = -1
        for j in range(0, n):
            if j not in a:
                smallest = j
                break
        if smallest == mex:
            print("yes")
        else:
            print("no")
    else:
        y = max(a)
        boo = True
        for j in range(n):
            if a[j] == -1:
                continue
            elif a[j] == max(a):
                continue
            else:
                boo = False
                print("no")
                break
        if y == 0:
            print("no")
        elif boo:
            print("yes")
