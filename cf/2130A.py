num = int(input())
for _ in range(num):
    num1 = int(input())
    x_list = list(map(int, input().split()))
    total = 0
    for x in x_list:
        if x > 0:
            total += x
        elif x == 0:
            total += 1
    
    print(total)
