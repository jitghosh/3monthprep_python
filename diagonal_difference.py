def diagonalDifference(arr):
    
    n = len(arr)
    diag_sum1 = 0
    diag_sum2 = 0
    for i in range(n):
        diag_sum1 += arr[i][i]
        diag_sum2 += arr[i][n-1-i]
    
    return abs(diag_sum1 - diag_sum2)