def countingSort(arr):
    freq_arr = [0]*100
    for val in arr:
        freq_arr[val] += 1
    return freq_arr
