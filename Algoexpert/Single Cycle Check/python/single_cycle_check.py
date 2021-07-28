# O(n) time | O(n) space
def hasSingleCycle_visited_list(array):

    n = jumps = len(array)
    visited = [0] * n

    curr_idx = 0

    while jumps >= 0:

        interval = array[curr_idx]

        next_idx = curr_idx + interval
        next_idx = next_idx % n

        print('jumps: ', jumps)
        print('interval: ', interval)
        print('next_idx: ', next_idx)

        if next_idx > n - 1: 
            next_idx = next_idx - n
        elif next_idx < 0:
            next_idx = n + next_idx
            
        print('corrected next_idx: ', next_idx)

        visited[next_idx] = 1
        curr_idx = next_idx
        print(visited)
        print()
        jumps -= 1

    print(visited)
    return sum(visited) == n

# O(n) time | O(1) space
def hasSingleCycle(array):
    
    numElementsVisited = 0
    currentIdx = 0
    
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
        
    return currentIdx == 0

def getNextIdx(currentIdx, array):

    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)

def main():
    
    array = [10, 11, -6, -23, -2, 3, 88, 909, -26]
    
    print(hasSingleCycle_visited_list(array))
    print(hasSingleCycle(array))
    
if __name__ == "__main__":
    main()
