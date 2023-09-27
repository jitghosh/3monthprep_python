from itertools import combinations

def maximumPerimeterTriangle(sticks):
    # take all combinations of size 3,
    # order does not matter so we use combinations and not permutations

    three_combos = list(combinations(sticks,3))
    # take only the combos that are valid triangles, 
    valid_three_combos = [combo for combo in three_combos if canBeTriangle(combo)]

    if len(valid_three_combos) == 0:
        return [-1]

    # sort each combo from max length side to min length side and also calc the sum, and return the combo and its sum as tuples
    combo_permiters = [(sorted(combo,reverse=True),sum(combo)) for combo in valid_three_combos]

    combo_permiters = sorted(combo_permiters, key = lambda tup: (-tup[1], -tup[0][0], -tup[0][2]))
    
    # answer in non-decreasing order (we previously sorted in decreasing order)
    return sorted(list(combo_permiters[0][0]))

def canBeTriangle(arrsides):
    # for any traingle - sum of two sides must be greater than the 3rd side
    if(arrsides[0] + arrsides[1] <= arrsides[2] or 
       arrsides[0] + arrsides[2] <= arrsides[1] or 
       arrsides[1] + arrsides[2] <= arrsides[0]):
        return False
    return True

maximumPerimeterTriangle([1,2,3,4,5,10])