def closestNumbers(arr):
    '''
    Once the array is sorted (ascending) we only need to calculate the differences of 
    numbers that are next to each other. The difference between any non neighbor numbers will 
    always be more than that of the immediate neighbors.
    '''
    arr = sorted(arr) #
    min_diff = None
    min_diff_pairs = []
    for i in range(0,len(arr) - 1):
        # if we are starting the loop or 
        # if we have encountered a min diff lower than the previous one
        if i == 0 or abs(arr[i+1] - arr[i]) < min_diff:
            # reset the diff and the pairs list
            min_diff = abs(arr[i+1] - arr[i])
            min_diff_pairs = [arr[i],arr[i+1]]
        # if we have encountered a min diff equal to the previous one
        # we record that pair as well
        elif abs(arr[i+1] - arr[i]) == min_diff:
            # add the pair to the pairs list
            min_diff_pairs += [arr[i],arr[i+1]]

    return min_diff_pairs


closestNumbers([int(val) for val in "-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854".split(" ")])