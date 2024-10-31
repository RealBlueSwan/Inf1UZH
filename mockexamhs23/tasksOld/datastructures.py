def add_grade(t1, num, subject, grade):
    # Check if tuple1 is empty then add the dict
    if not t1:
        return {num: {subject: grade}}
    
    # Check if keys are the same
    if t1.get(num) == None:
        t1[num] = {subject: grade}
        return t1
    
    else: 
        if t1[num].get(subject) == None:
            t1[num][subject] = grade
            return t1
        
        else:
            return t1                   


def remove_grade(t1, num, subject):
    if not t1:
        return {}
    
    if num in t1 and subject in t1[num]:
        del t1[num][subject]
        if not t1[num]:  # If the dictionary for the student is empty, remove the student
            del t1[num]
    return t1

#print( add_grade(   {},                                    111, "INF-1", 4.00) )           #   {111: {'INF-1': 4.0}}
#print( add_grade(   {222: {"INF-1": 3.50}},                222, "PHY-2", 5.50) )           #   {222: {'INF-1': 3.5, 'PHY-2': 5.5}}
#print( add_grade(   {222: {"INF-1": 3.50}},                333, "PHY-2", 1.75) )           #   {222: {'INF-1': 3.5}, 333: {'PHY-2': 1.75}}
#print( remove_grade({222: {"INF-1": 3.50, "PHY-2": 5.50}}, 222, "INF-1") )                 #   {222: {'PHY-2': 5.5}}
#print( remove_grade({222: {"INF-1": 3.50}},                222, "INF-1") )                 #   {}
#print( remove_grade({222: {"INF-1": 3.50, "PHY-2": 5.50}}, 111, "INF-1") )                 #   {222: {'INF-1': 3.5, 'PHY-2': 5.5}}
#print( remove_grade({},                                    111, "INF-1") )                 #   {}