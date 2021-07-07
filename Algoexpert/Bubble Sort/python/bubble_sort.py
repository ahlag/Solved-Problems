def bubbleSort_unoptimized(array):
    
    n = len(array)
	
    for i in range(n-1):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array

def bubbleSort_optimized(array):
    
    n = len(array)
    
    for i in range(n):
        
        swapped = False
        
        for j in range(0, n - i - 1):
            
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
                swapped= True
            
        if not swapped:
            break
        
    return array

def main():
    
    array = [8, 5, 2, 9, 5, 6, 3]
    
    print(bubbleSort_unoptimized(array))
    print(bubbleSort_optimized(array))
    
    
if __name__ == "__main__":
    main()