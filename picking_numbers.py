def pickingNumbers(a):
    '''
    The subarray we need is has absolute diff between any two elements <= 1. 
    Also note that the subarray is not necessarily contigous. 
    Sort the subarray first. This way you will not encounter a sitation where some 
    number violates the constraint - but then there are numbers after it that do not.
    Idea : The abs(sum) of the signed differences as we iterate through the list 
    has to be <= 1 as well as individual abs(diffs) have to be <= 1 for as long as the subarray 
    satisfies this condition. When it is not is we skip that number and continue.
    Ex: 1,1,2,2,3,2,2 is a list. 
    The differences are 0(1-1), 1(2-1), 0(2-2), 1(3-2), -1(2-3), 0(2-2)
    If we cumulatively add these differences when we reach 3, the sum is 2. 
    So our subarry ends at 1,1,2,2
    '''
    a = sorted(a)
    cum_sum = 0
    subarray_lengths = []
    subarrays = [] # do not need this
    for idx1 in range(0,len(a) - 1):
        subarray = [a[idx1]]
        cum_sum = 0
        for idx2 in range(idx1 + 1,len(a)):
            diff = a[idx2] - subarray[-1]
            if (abs(diff) <= 1 and abs(cum_sum + diff) <= 1):
                subarray.append(a[idx2])
                cum_sum += diff
        subarray_lengths.append(len(subarray))
        subarrays.append(subarray) # do not need this - but good for debugging
    
    return max(subarray_lengths)  

print(pickingNumbers([int(val) for val in "4 2 3 4 4 9 98 98 3 3 3 4 2 98 1 98 98 1 1 4 98 2 98 3 9 9 3 1 4 1 98 9 9 2 9 4 2 2 9 98 4 98 1 3 4 9 1 98 98 4 2 3 98 98 1 99 9 98 98 3 98 98 4 98 2 98 4 2 1 1 9 2 4".split(" ")]))
#print(pickingNumbers([4,6,5,3,3,1])) # longest is 4,3,3
#print(pickingNumbers([1,2,2,3,1,2])) # longest is 1,2,2,1,2
#print(pickingNumbers([98,3,99,1,97,2])) # longest is 98,99 or 1,2