def birthday(s, d, m):
    startat = 0
    ctr = 0
    # contingous - so we need to check slices starting from 0th, moving the slice right one item at a time
    # i.e check 0 to m-1, 1 to m, 2 to m+1 and so on until the right sie of the slice is at the tail of the list
    while startat + m <= len(s):
        if sum(s[startat:startat + m]) == d:
            ctr += 1
        startat += 1
    
    return ctr