def pangrams(s):
    uniques = set() 
     
    for c in s.lower(): # let's make the case uniform
        uniques.add(c)
    
    for c in range(97,123): # ascii range for lower case alphabet is 97 - 122 - or you could also use a list like ['a','b',...] 
        if chr(c) not in uniques:
            return "not pangram" # not a pangram - some character is missing
    
    return "pangram"
