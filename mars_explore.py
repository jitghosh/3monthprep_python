def marsExploration(s): 
    num_sos = int(len(s)/3)
    num_wrong = 0
    for i in range(num_sos):
        slice = s[i*3 : i*3 + 3]
        if slice[0] != "S":
            num_wrong += 1
        if slice[1] != "O":
            num_wrong += 1
        if slice[2] != "S":
            num_wrong += 1
    
    return num_wrong