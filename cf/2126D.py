num = int(input())
for i in range(num):
    n, k = map(int, input().split())
    lst = []
    for j in range(n):
        a = list(map(int, input().split()))
        lst.append(a)
    lst = sorted(lst, key = lambda x: (x[0], x[1]))
    for l in range(n):
        if k < lst[l][0]:
            break
        elif lst[l][2] > k:
            k = lst[l][2]
    print(k)
