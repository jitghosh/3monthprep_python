from itertools import combinations

def minimumAbsoluteDifference(arr):
    '''
    once the list is sorted (Ascending), then the diffs between the subsequent numbers 
    are the least possible and any other pairs that are not side by side need not be considered.
    and we take their min. E.g.:
    -9,-6, -3, 1,5,7,8,10. In this list the diff between say -9 and -3 need not be considered as 
    the diff between -9 and -6 will always be less gien that the list is sorted.
    '''
    arr = sorted(arr)
    return min([abs(arr[i+1] - arr[i]) for i in range(0,len(arr) - 1)])

with open("test_min_abs_diff.txt","r") as datafile:
    data = datafile.readline()

print(minimumAbsoluteDifference([int(d) for d in data.split(" ")]))