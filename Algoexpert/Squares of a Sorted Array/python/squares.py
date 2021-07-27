def sortedSquaredArray(array):

    result = [0] * len(array)

    array = sorted(array, key=lambda x: abs(x))

    for i in range(len(array)):
        result[i] = array[i] ** 2

    return result


def main():
    
    array = [75, 105, 120, 75, 90, 135]
    
    print(sortedSquaredArray(array))
    
if __name__ == "__main__":
    main()