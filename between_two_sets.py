def getTotalX(a, b):
    upper = max(b)
    lower = min(a)
    retval = 0
    for num in range(lower, upper):
        if all([num % factor == 0 for factor in a]) and all([multiple % num == 0 for multiple in b]):
            retval += 1
    
    return retval

print(getTotalX([1],[100]))