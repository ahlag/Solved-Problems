# O(n) time | O(n) space
def isValidSubsequence(array, sequence):

    seqIdx = 0

    for i in range(len(array)):

        if array[i] == sequence[seqIdx]:
            seqIdx += 1

        if seqIdx == len(sequence):
            break

    return seqIdx == len(sequence)

# O(n) time | O(1) space
def isValidSubsequence_while(array, sequence):
    
    arrIdx = 0
    seqIdx = 0
    
    while arrIdx < len(array) and seqIdx < len(sequence):
        
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
        
    return seqIdx == len(sequence)

def main():
    
    array = [5, 1, 22, 25, 6, -1, 8, 100]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))
    
    print(isValidSubsequence_while(array, sequence))
    
if __name__ == "__main__":
    main()