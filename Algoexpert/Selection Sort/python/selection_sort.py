# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst O(n^2) time | O(1) space
def selectionSort(array):
    
	n = len(array)
	curr_idx = 0
	
	while curr_idx < n - 1:
		smallest_idx = curr_idx
		for i in range(curr_idx + 1, n):
			if array[smallest_idx] > array[i]:
				smallest_idx = i
    
		if curr_idx != smallest_idx:
			array[curr_idx], array[smallest_idx] = array[smallest_idx], array[curr_idx]

		curr_idx += 1

	return array

def main():
    
    array = [8, 5, 2, 9, 5, 6, 3]
    
    print(selectionSort(array))    
    
if __name__ == "__main__":
    main()