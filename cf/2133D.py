t = int(input())
def solve(h):
    prev2 = 0 #min num of attack 2 steps before
    prev1 = h[0] #min num of attack 1 step before
    a = None
    b = None
    for i in range(1,len(h)):
        a = h[i] - 1 + prev1 # min num of attack in prev 1, make it fall, then kill it directly
        b = h[i-1] + prev2 + max(0, h[i]-(i)) # kill the mob right below it, make it fall and kill the remaining health and min num of attack in prev 2
        prev2 = prev1
        prev1 = min(a,b)
    return prev1
    
    
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    print(solve(h))
