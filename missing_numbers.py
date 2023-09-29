from collections import Counter
def missingNumbers(arr, brr):
    # calculate the frequencies in each list
    counter_arr = Counter(arr)
    counter_brr = Counter(brr)

    missing_nums = []
    keys_arr = list(counter_arr.keys())
    keys_brr = list(counter_brr.keys())

    for key in keys_brr:
        # either the number is missing completely 
        # or it occurs more number of times in brr
        if (key not in keys_arr) or counter_brr[key] > counter_arr[key]:
            missing_nums.append(key)
    
    return sorted(missing_nums)