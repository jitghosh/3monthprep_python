from collections import deque

def countingValleys(steps, path):
    # using deque as stack
    m_count = 0
    v_count = 0
    path_stack = deque()
    path_stack.append(path[0])
    for c in path[1:]:
        if len(path_stack) > 0 and path_stack[-1] != c:
            path_stack.pop()
            if len(path_stack) == 0: # sea level
                if c == "U": # stepping up to sea level 
                    v_count += 1
                else:
                    m_count += 1

        else:
            path_stack.append(c)
    return v_count
