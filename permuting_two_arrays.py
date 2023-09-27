from collections import Counter
from itertools import accumulate

def twoArrays(k, A, B):
    '''
    Say A = [1,2,2,1,2]
    and B = [3,4,2,1,2]
    and k = 4
    k - B = [1,0,2,3,2]

    So we need in A at least one number >= 3, 
    at least two numbers >= 2 (not including the previous ones), 
    at least one number >= 1 (not including the previous ones) and 
    at least one number >= 0 (not including the previous ones)

    But A does not satisfy this - hence no permutation will work

    Note that we need to start evaluating in descending order. Otherwise in the previous example 
    say if we evaluate 2 before 3, and there was only one 2, we will end up counting 3 as a number >= 2 as well 
    and satisfy the question and then also satisfy the question at least one >= 3 - thus double counting 3.
    
    '''
    lst = sorted(A, reverse=True) # descending order
    counter_diff_B = Counter([k - val for val in B ]) # take the diff k - B and store the counts
    # go over the nums in descending order 
    for k in sorted(counter_diff_B.keys(), reverse=True):
        lst, Ok = FindCountAndRemove(lst,k,counter_diff_B[k])
        if not Ok:
            return "NO"
    
    return "YES"


def FindCountAndRemove(lst, num, count):
    '''
    lst is already sorted descending. check to see if we 
    have at least "count" values starting from the beginning that are >= num. If so we are good. 
    Remove those values and return the list so that next time around we do not double count
    '''
    if lst[:count][-1] >= num: # we have at least "count" values in lst that are >= num 
        return lst[count:], True
    else:
        return None, False

print(twoArrays(4,[1,2,2,1,2],[3,4,2,1,2]))
    