import math
 
def lcm(x, y):
    return x * y // math.gcd(x, y)
 
n = int(input())
for _ in range(n):
    size = int(input())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))
    
    tracker = True
 
    # Validate monotonicity and divisibility
    for j in range(1, size):
        if p[j] > p[j-1] or p[j-1] % p[j] != 0:
            print("NO")
            tracker = False
            break
        if s[j] < s[j-1] or s[j] % s[j-1] != 0:
            print("NO")
            tracker = False
            break
 
    if not tracker:
        continue
 
    # Main logic: build lcm array and verify gcds
    a = [lcm(p[i], s[i]) for i in range(size)]
 
    g = a[0]
    pos = True
    for i in range(size):
        g = math.gcd(g, a[i])
        if g != p[i]:
            pos = False
            break
 
    if pos:
        g = a[-1]
        for i in range(size - 1, -1, -1):
            g = math.gcd(g, a[i])
            if g != s[i]:
                pos = False
                break
 
    print("YES" if pos else "NO")
