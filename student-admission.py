# application -> University -> approve

# INPUT DATA
student_SCHOOL_MARK    = 6.0  # float
UNIVERSITY_MARK        = 7.0  # float

UNIVERSITY_contract   =10000  # int/ year
student_Money         = 2000 
student_DAD_HAS_CONN  = True

# Logic
mark_condition = student_SCHOOL_MARK >= UNIVERSITY_MARK
money_condition = student_Money >= UNIVERSITY_contract
conn_condition = student_DAD_HAS_CONN 

approved = mark_condition  or money_condition or conn_condition

# Output
print( "Will the student be approved", approved)


