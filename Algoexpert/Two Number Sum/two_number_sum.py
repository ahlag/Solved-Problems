## array = [3, 5, -4, 8, 11, 1, -1, 6]
## targetSum = 10
## Output: [-1, 11]

## Brute Force
def brute_force(array, targetSum):
    
    n = len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
            
    return []

## O(n logn)
def binary_search(array, targetSum):
    
    array.sort()
    l, r = 0, len(array) - 1
    
    while l < r:
        
        curr_sum = array[l] + array[r]
        
        if curr_sum == targetSum:
            return [array[l], array[r]]
        else:
            if curr_sum < targetSum:
                l += 1
            else:
                r -= 1
        
    return []

## 0(n)
def hash_table(array, targetSum):
    
    hash_table = {}
    n = len(array)
    
    for x in array:
        y = targetSum - x
        if y in hash_table:
            return [x, y]
        else:
            hash_table[x] = True 
            
    return []

def main():
    
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    
    print(brute_force(array, targetSum))
    print(binary_search(array, targetSum))
    
if __name__ == "__main__":
    main()
    