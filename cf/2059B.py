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
        cost = 2    # the idea why 2 is chosen is shown below
        for p in range(1, n - 2 * k + 2):  # inclusive up to n - 2k + 1
            if a[p] != 1:
                cost = 1
                break
 
    print(cost)



'''
Idea and a "proof"

case 1:
if n == 2*k, trivial. we just have to iterate through the list because there is no other way to group the elements

case 2:
suppose n != 2*k
if the first n-2k+2 ele is not 1, 1 must be the min cost because we can group the second subarray onwards as a subarray that contains one element each.
why n-2k+2? to ensure we still meet the requirement of the k subarray by letting the remaining element be 1 subarray containing 1 element each.
now 2 must be the min cost, that is when the first n-2k+2 element must be 1. 
suppose 2 is not the min, say 3 is the min, we can simply partition say the first n-2k+2 ele into say [n-2k] subarray and [2] subarray. 
notice that [2] subarray = [1,1] and hence, b1=1, b2!=2, thus cost = 2, contradiction that 3 is the min!

'''
