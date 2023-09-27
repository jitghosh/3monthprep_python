# Enter your code here. Read input from STDIN. Print output to STDOUT

def combine(line: str):
    type_hint = line[0]
    value = line[2:]
    name:str = ""
    if type_hint == "V":
        name = "".join([val if idx == 0 else val.capitalize() for idx,val in enumerate(value.split())])
    elif type_hint == "C":
        name = "".join([val.capitalize() for idx,val in enumerate(value.split())])
    elif type_hint == "M":
        name = "".join([val if idx == 0 else val.capitalize() for idx,val in enumerate(value.split())])+"()"
    print(name)

def split(line: str):
    type_hint = line[0]
    

    if line[0] == "M":
        value = line[2:-2]
    else:
        value = line[2:]

    caps_idx = [idx for idx,c in enumerate(value) if c.isupper()]
    if caps_idx[0] != 0:
        caps_idx.insert(0,0)
    zipped_idx_ranges = zip(caps_idx,caps_idx[1:]+[None])
    parts = [value[i:j].lower() for i,j in zipped_idx_ranges]
    
    print(" ".join(parts))
    
if __name__ == "__main__":
    try:
        while True:
            line = input()
            if line.startswith("C"):
                combine(line[2:])
            elif line.startswith("S"):
                split(line[2:])
    except (EOFError):
        exit(0)