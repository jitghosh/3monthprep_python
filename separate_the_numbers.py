def separateNumbers(s: str):
    '''
    Fact 1: For two numbers to have a difference of 1, 
    the numbers will either have to have the same number of digits 
    or one may be longer than the other by at most one digit (100 - 99 = 1). 
    A difference in length any longer than that yield a difference 
    greater than 1 when the numbers are subtracted.

    Fact 2: If the number of digits(n) are even tha max num of digits any subinteger can have 
    is n/2. E.g. "131132" -> 132 - 131 = 1. max digits of subinteger = 3.
    For odd digits, this is n//2 and n//2 + 1.
    E.g. "9991000" -> 1000 - 999 = 1. max digits are 3 and 4. (7//2 and 7//2 + 1) 

    Approach:
    We loop through substring sizes starting from 1 to num_digits//2 (See Fact 2). For each of those
    we recursively evaluate if the diff between a subinteger of current sibstring size and the next 
    subinteger of this size or size + 1 is equal to 1. We keep recursing until the condition fails or we 
    exhaust the string. We return true if we exhaust the string without failing the condition.
    We record the first substring in the loop and that is our minimum snce the substrings will have to 
    be in ascending order for our condition to hold.  
    '''
    for l in range(1,len(s)//2 + 1):
        min = s[0:l]
        if not process(s[l:],min):
            continue
        else:
            print(f"YES {min}")
            return
    
    print("NO")

def process(remaining_s: str,prev_num_s: str):
    # remaining number of digits is less than the previous subinteger - 
    # so condition fails
    if len(remaining_s) < len(prev_num_s):
        return False
    # given problem constraint
    elif remaining_s.startswith("0"):
        return False
    
    prev_num = int(prev_num_s)
    prev_num_len = len(prev_num_s)

    # condition holds comparing with the next subinteger of the same size
    if int(remaining_s[0:prev_num_len]) - prev_num == 1:
        # and we have consumed all of what was remaining - 
        # so nothing to process any more (recursion base condition)
        if len(remaining_s) == prev_num_len:
            return True
        else: # recurse
            return process(remaining_s[prev_num_len:],remaining_s[0:prev_num_len])
    # condition holds comparing with the next subinteger of size greater by 1 digit
    elif int(remaining_s[0:prev_num_len + 1]) - prev_num == 1:
        # and we have consumed all of what was remaining - 
        # so nothing to process any more (recursion base condition)
        if len(remaining_s) == prev_num_len + 1:
            return True
        else: # recurse
            return process(remaining_s[prev_num_len + 1:],remaining_s[0:prev_num_len + 1])
        

print(separateNumbers("99100"))
print(separateNumbers("979899100101"))
print(separateNumbers("1234467"))

