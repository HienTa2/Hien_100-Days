# new_list = [new_item for item in list]

# [expression for item in iterable if condition]
#
# # Let's say we have a list of numbers
# numbers = [1, 2, 3, 4, 5, 6]
#
# # And we want a new list where each number is squared
# squared_numbers = [number ** 2 for number in numbers]
#
# # Now squared_numbers is [1, 4, 9, 16, 25, 36]
#
#
# # dictionary comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import pandas

student_dict = {
    "student": ['Angela', 'James', 'Lily'],
    "score": [56, 76, 98]
}

# Looping through dictionary
# for (key, value) in student_dict.items():
#     print(value)

# Dataframe
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through datafram
for (index, row) in student_data_frame.iterrows():
    print(row.student)

