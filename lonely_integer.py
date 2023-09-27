def lonelyinteger(a):
    count_dict = {}
    for val in a:
        if val in count_dict:
            count_dict[val] += 1
        else:
            count_dict[val] = 1
    
    for key in count_dict:
        if count_dict[key] == 1:
            return key 