def matchingStrings(strings, queries):
    counts = [0]*len(queries)
    for idx,q in enumerate(queries):
        for s in strings:
            if s == q:
                counts[idx] += 1
    return counts