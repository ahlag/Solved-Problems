def sortedSquaredArray(array):

    result = [0] * len(array)

    array = sorted(array, key=lambda x: abs(x))

    for i in range(len(array)):
        result[i] = array[i] ** 2

    return result

def sortedSquaredArray_two_pointers(nums):

    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result


def main():
    
    array = [75, 105, 120, 75, 90, 135]
    
    print(sortedSquaredArray(array))
    
    print(sortedSquaredArray_two_pointers(array))
    
if __name__ == "__main__":
    main()