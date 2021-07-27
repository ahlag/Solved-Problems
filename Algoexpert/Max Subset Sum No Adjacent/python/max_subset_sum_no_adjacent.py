# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    
    n = len(array)
    
    if n == 0:
        return 0
    elif n == 1:
        return array[-1]
    
    maxsums = array[:]
    maxsums[1] = max(array[0], array[1])
    
    for i in range(2, n):
        maxsums[i] = max(maxsums[i-1], array[i] + maxsums[i-2])
        
    return maxsums[-1]

# O(n) time | O(1) space
def maxSubsetSumNoAdjacent_linear_space(array):
    
    n = len(array)
    
    if n == 0:
        return 0
    elif n == 1:
        return array[0]
    
    second  = array[0]
    first = max(array[0], array[1])
    
    for i in range(2, n):
        current = max(first, array[i] + second)
        second = first
        first = current
        
    return current

def main():
    
    array = [75, 105, 120, 75, 90, 135]
    
    print(maxSubsetSumNoAdjacent(array))
    print(maxSubsetSumNoAdjacent_linear_space(array))
    
if __name__ == "__main__":
    main()