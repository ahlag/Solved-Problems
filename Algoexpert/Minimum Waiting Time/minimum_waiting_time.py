def minimumWaitingTime(queries):

    queries.sort()
    time_taken = 0
    for i in range(len(queries)-1):
        time_taken += sum(queries[0:i+1])
        
    return time_taken

def minimumWaitingTime_enumeration(queries):
    
    queries.sort()

    time_taken = 0
    for i, duration in enumerate(queries):
        queries_left = len(queries) - (i + 1)
        time_taken += duration * queries_left

    return time_taken

def main():
    
    array = [3, 2, 1, 2, 6]
    
    print(minimumWaitingTime(array))
    print(minimumWaitingTime_enumeration(array))
    
if __name__ == "__main__":
    main()