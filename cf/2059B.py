t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k = k // 2
 
    cost = k + 1
 
    if n == 2 * k:
        for p in range(1, n, 2):  # 1, 3, 5, ...
            if a[p] == (p + 1) // 2:
                continue
            else:
                cost = (p + 1) // 2
                break
    else:
        cost = 2
        for p in range(1, n - 2 * k + 2):  # inclusive up to n - 2k + 1
            if a[p] != 1:
                cost = 1
                break
 
    print(cost)


# Idea and proof
