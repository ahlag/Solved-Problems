def binary_search_iterative(array, target):
    
    l, r = 0, len(array) - 1
    
    while l <= r:
        
        mid = (l + r)//2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            r = mid - 1
        elif array[mid] < target:
            l = mid + 1
    
    return -1

def binary_search_recursive(array, target):
    
    return binary_search_recursive_helper(array, target, 0, len(array) - 1)

def binary_search_recursive_helper(array, target, l, r):
    
    if l > r:
        return -1
    
    mid = (l + r) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search_recursive_helper(array, target, mid + 1, r)
    elif array[mid] > target:
        return binary_search_recursive_helper(array, target, l, mid - 1)
    
def main():
    
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    
    print(binary_search_iterative(array, target))
    print(binary_search_recursive(array, target))
    
    assert(binary_search_iterative(array, target) == binary_search_recursive(array, target))
    
if __name__ == "__main__":
    main()