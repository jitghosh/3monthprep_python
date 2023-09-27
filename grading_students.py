def gradingStudents(grades):
    return [round_grade(g) for g in grades]

def round_grade(grade):
    if grade < 38:
        return grade
    
    if grade % 5 != 0:
        nm = next_multiple_of(grade,5)
        if nm - grade < 3:
            return nm
        else:
            return grade
    
    return grade
         
def next_multiple_of(num, multipleOf):
    while num % multipleOf != 0:
        num += 1
    
    return num