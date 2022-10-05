new_dict={
       'Student_info':
           {
               'student_name':'Peter',
               'T_name':'Alex'
           },
       'student_age':30,
       'student_position':'Topper',
       'addr':
           {
           'student_City':'Los Angeles',
           'Country':'U.S.A'
           }      
      }
student_length = len(new_dict)
for a in new_dict.values():
    if isinstance(a, dict):
        student_length += len(a)
print("length of the dictionary is", student_length)