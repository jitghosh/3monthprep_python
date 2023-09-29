def maxMin(k, arr):
    '''
    Once the array is sorted, for any k-length slice of the array, 
    the fairness is the (last item - first item) of that slice. 
    Once we calculate all these fairness values, there cannot be any fairness
    values smaller than the minimum of these. If there was either 
    the largest or smallest value used in calculating such a fairness 
    would have fallen in one of the slices of the sorted array.
    '''
    arr = sorted(arr)
    min_fairness = None
    for i in range(0,len(arr) - k + 1):
        slice = arr[i:i+k]
        if min_fairness == None:
            min_fairness = slice[-1] - slice[0]
        else:
            min_fairness = min(min_fairness,slice[-1] - slice[0])
    return min_fairness
