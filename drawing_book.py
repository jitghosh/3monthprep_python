def pageCount(n, p):
    
    if p - 1 < n - p: # p is closer to the front - so start from the front to get min page turns
        # example (1), (2,3), (4,5), (6,7), (8,9),...say p = 8 (or 9) 
        # either case we need 4 page turns starting from the front i.e. 8//2 or 9//2
        return p // 2 
    else: # start from the back
        if n % 2 != 0: #even num pages
            # example (1),(2,3),(4,5) .. (12,13), (14,15), (16,17), (18,19), (20,21),...say p = 13 or 12
            # either case we need 4 page turns starting from the back i.e. (21 - 12)//2 or (21 - 13)//2
            return (n - p)//2
        else:
            # example (1),(2,3),(4,5) .. (12,13), (14,15), (16,17), (18,19), (20),...say p = 13 or 12
            # either case we need 4 page turns starting from the back i.e. (20 + 1 - 12)//2 or (20 + 1 - 13)//2
            return (n + 1 - p)//2