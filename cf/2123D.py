num = int(input())
for i in range(num):
    n, k = map(int, input().split())
    s = str(input())
    sum = 0
    for i in range(n):
        sum+=int(s[i])
    if sum <= k:
        print("alice")
    elif 2*k-1 >= n:
        print("alice")
    else:
        print("bob")



'''
idea:

when total num of 1 is less than k, alice can simply make all the 1 into 0 immediately.
when the string is long enough, specifically when n+1/2 >= k, 
alice can simply put one 0 at the furthest end of the string each round to slowly win off the game.

'''
