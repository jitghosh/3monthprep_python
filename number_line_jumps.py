def kangaroo(x1, v1, x2, v2):
    '''
    One way would be to keep looping where each iteration is a jump,
    while progressing both kangaroos through the number line based on 
    their start and rate.
    But this is not a good idea since if the kangaroos never meet, the loop will 
    continue infinitely.

    Let's use math instead. Let's assume that after k jumps - the kangaroos meet.
    So then x1 + k*v1 = x2 + k*v2. Solving: k = (x2 - x1)/(v1 - v2). If k is a positive 
    integer (since we cannot have fractional jumps) then the answer is yes.

    One way we can check this - the divisor is non zero, no remainder from the division 
    and the result > 0
    '''

    return "YES" if (v1 - v2) > 0 and ((x2-x1) % (v1-v2)) == 0 and ((x2-x1) / (v1-v2)) > 0 else "NO"
