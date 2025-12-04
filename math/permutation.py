# generating all possible permutations of nums
# nums is an array of distinct integer [x1, x2, ..., xn] 
def permute(nums):
    ans, sol = [],[]
    def backtrack():
        if len(sol) == len(nums):
            ans.append(sol[:])
            return
        for num in nums:
            if num not in sol:
                sol.append(num)
                backtrack()
                sol.pop()
    
    backtrack()
    return ans
