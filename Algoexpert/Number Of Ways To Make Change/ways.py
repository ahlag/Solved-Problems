## C: Coin Value
## Time O(CN) | Space O(CN)
def two_dimensional_dp(n, denoms):
	
    size = len(denoms)
    # Declaring a 2-D array
    # for storing solutions to subproblems:
    dp = [[0 for i in range(n+1)] for i in range(size+1)]

    # Initializing first column of array to 1
    # because a sum of 0 can be made
    # in one possible way: {0}
    for i in range(size + 1):
        dp[i][0] = 1

    # Applying the recursive solution:
    for i in range(1, size+1):
        for j in range(1, n+1):
            
            # Cannot pick the highest coin:
            if denoms[i-1] > j:
                dp[i][j] = dp[i - 1][j]
                
            # Pick the highest coin:
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - denoms[i-1]]

    return dp[size][n]

def one_dimensional_dp(n, denoms):
    
    dp = [0 for amount in range(n+1)]
    dp[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                dp[amount] += dp[amount - denom]

    return dp[n]

def main():
    
    n = 6
    denoms = [1, 5]
    print(two_dimensional_dp(n, denoms))
    
    print(one_dimensional_dp(n, denoms))
    
if __name__ == "__main__":
    main()
