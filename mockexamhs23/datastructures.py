# Implement both functions. Change the method signatures to add parameters as specified!
# Remember to return grades at the end of each function!

def add_grade(grades, mnum, course, grade):
    # check if key exists, else create new key. 
    # check if mnum is same
    for n in grades: 
        if mnum == n: 
            return None
            
    # add value
    t1 = {course: grade}
    grades[mnum] = t1

    return grades


def remove_grade():
    pass


print( add_grade(   {},                                    111, "INF-1", 4.00) )
print( add_grade(   {222: {"INF-1": 3.50}},                222, "PHY-2", 5.50) )
#print( add_grade(   {222: {"INF-1": 3.50}},                333, "PHY-2", 1.75) )
#print( remove_grade({222: {"INF-1": 3.50, "PHY-2": 5.50}}, 222, "INF-1") )
#print( remove_grade({222: {"INF-1": 3.50}},                222, "INF-1") )
#print( remove_grade({222: {"INF-1": 3.50, "PHY-2": 5.50}}, 111, "INF-1") )
#print( remove_grade({},                                    111, "INF-1") )

#{111: {'INF-1': 4.0}}
#{222: {'INF-1': 3.5, 'PHY-2': 5.5}}
#{222: {'INF-1': 3.5}, 333: {'PHY-2': 1.75}}
#{222: {'PHY-2': 5.5}}
#{}
#{222: {'INF-1': 3.5, 'PHY-2': 5.5}}
#{}
