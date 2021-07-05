from copy import deepcopy

## Check Cracking the code interview solution #1
## O(n 2^n)
def powerset_recursive(parent_set, index=None):
    
    ## If index is not intialized to the size of parent_set
    if index is None:
        index = len(parent_set) - 1
        
    if index == -1:
        return [[]]
    
    old_subsets = powerset_recursive(parent_set, index - 1)
    new_subsets = []
    item = parent_set[index]
    
    ## e.g. P(2) = {}, {a1}, {a2}, {a1, a2}
    ##      P(3) = {}, {a1}, {a2}, {a3}, {a1, a2}, {a1, a3}, {a2, a3}, {a1, a2, a3}
    ## P(3) - P(2) = {a3}, {a1, a3}, {a2, a3}, {a1, a2, a3}
    ## So, we add a3 to the old subset of P2 to get the differnce
    ## P(2)      = {}, {a1}, {a2}, {a1, a2}
    ## P(2) + a3 = {a3}, {a1, a3}, {a2, a3}, {a1, a2, a3}
    ## Then, we simply clone P2 to P(2) + a3 to get the complete subset
    for element in old_subsets:
        new_subsets.append(element)
        entry = deepcopy(element)
        entry.append(item)
        new_subsets.append(entry)
    
    return new_subsets

## Check Approach 1 of https://www.techiedelight.com/generate-power-set-given-set/
def powerset_backtrack(parent_set, subsets, choice=[], index=None):
    
    if index is None:
        index = len(parent_set)
        
    if index == 0:
        entry = deepcopy(choice)
        subsets.append(entry)
        return
        
    choice.append(index)
    powerset_backtrack(parent_set, subsets, choice, index-1)
        
    choice.pop()
    
    powerset_backtrack(parent_set, subsets, choice, index-1)
    
## Powerset bitwise / Combinatronics
## Check Approach 2 of https://www.techiedelight.com/generate-power-set-given-set/
def powerset_bitwise(parent_set):
    
    ## N stores the total number of subsets
    N = int(pow(2, len(parent_set)))
    element = set()
    subsets = []
    
    ## Generate each subset one by one
    for i in range(N):
        ## Check every bit of `i`
        for j in range(len(parent_set)):
            if i & (1 << j):
                element.add(parent_set[j])
                
        entry = deepcopy(list(element))
        subsets.append(entry)
        element.clear()
        
    return subsets

## Recursion Alternative Approach
## https://github.com/careercup/CtCI-6th-Edition-Python/blob/394a5b2e0ed8df465f600bd1f52c14705b4edb31/chapter_08/p04_power_set.py#L46-L60
def powerset_recursion_alternative(parent_set):
    subsets = [[]]

    def recurse(current_set, remaining_set):
        if len(remaining_set) == 0:  # base case
            return

        for i in range(len(remaining_set)):
            if current_set + [remaining_set[i]] not in subsets:
                subsets.append(current_set + [remaining_set[i]])
                recurse(current_set + [remaining_set[i]], remaining_set[i + 1 :])

    recurse([], parent_set)
    
    return subsets

testable_functions = [powerset_recursive, powerset_backtrack, powerset_bitwise]

test_cases = [({1, 2, 3}, {(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)})]

def test_get_subsets():
    for input_set, expected in test_cases:
        for get_subsets in testable_functions:
            results = get_subsets(list(input_set))
            results = {tuple(s) for s in results}
            assert results == expected
    
def main():
    parent_set = [1, 2, 3]
    subsets = []
    print(powerset_recursive(parent_set))
    powerset_backtrack(parent_set, subsets)
    print(subsets)
    print(powerset_bitwise(parent_set))
    print(powerset_recursion_alternative(parent_set))
    
if __name__ == "__main__":
    main()