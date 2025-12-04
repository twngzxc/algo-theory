# n!
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# nPr
def permutation(n, r):
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid values for n and r")
    return factorial(n) // factorial(n - r)

# nCr
def combination(n, r):
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid values for n and r")
    return factorial(n) // (factorial(r) * factorial(n - r))



# generating all possible combinations of size k from numbers 1 to n
# version 1 top down 
ans = [] # need to initialize this for version 1
def combination(n,k,sol,ans):
    if len(sol) == k:
        ans.append(sol[:])
        return
    elif n == 0:
        return
    else:
        # skip n
        combination(n-1,k,sol, ans)
        
        # include n
        sol.append(n)
        combination(n-1,k,sol,ans)
        # Must undo the append because 'sol' is a shared mutable list across recursion.
        # Without popping, the change persists into other branches (due to referencing),
        # causing incorrect combinations and infinite recursion.
        sol.pop()
    return ans  
# example: print(combination(4,2,[],ans))


# version 2 top down 
def combinations(n, k, sol=None, ans=None):
    if sol is None:
        sol = [] # initialize current working list
    if ans is None:
        ans = [] # initialize result list

    if len(sol) == k:
        ans.append(sol[:])
        return ans
    
    if n == 0:
        return ans

    # skip n
    combinations(n-1, k, sol, ans)

    # include n
    sol.append(n)
    combinations(n-1, k, sol, ans)
    sol.pop()  # backtrack

    return ans
# example: print(combinations(4,2))


# version 3 bottom up recursive
def combination_bottom_up_recursive(n, k, start=1, sol=None, ans=None):
    if sol is None:
        sol = []
    if ans is None:
        ans = []

    # Base case: combination complete
    if len(sol) == k:
        ans.append(sol[:])
        return ans

    # Stop if start exceeds n
    if start > n:
        return ans

    # Option 1: include start
    sol.append(start)
    combination_bottom_up_recursive(n, k, start + 1, sol, ans)
    sol.pop()  # backtrack

    # Option 2: skip start
    combination_bottom_up_recursive(n, k, start + 1, sol, ans)

    return ans
# example: print(combination_bottom_up_recursive(4, 2))


# version 4 bottom up iterative
def combination_bottom_up_iterative(n, k):
    # Start with an empty combination
    ans = [[]]

    # For each number from 1 to n
    for num in range(1, n + 1):
        new_combs = []
        for comb in ans:
            # Only extend combinations that have fewer than k elements
            if len(comb) < k:
                new_combs.append(comb + [num])
        ans += new_combs  # Add the new combinations to the list

    # Keep only combinations of exact size k
    return [comb for comb in ans if len(comb) == k]

# example: print(combination_bottom_up_iterative(4, 2))
