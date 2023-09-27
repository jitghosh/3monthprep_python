def divisibleSumPairs(n, k, ar):
    ctr = 0
    # outer loop goes to last but 1, inner loop goes to last so that the last pair we test for is (last but 1, last)
    for idx, val1 in enumerate(ar[:-1]): 
        # inner loop starts one after the current position in the outer loop since i has to be < j
        for val2 in ar[idx+1:]:
            if ((val1 + val2) % k) == 0:
                ctr += 1

    return ctr


print(divisibleSumPairs(6,3,[1,3,2,6,1,2]))