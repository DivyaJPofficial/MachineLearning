# Create an empty dictionary called dog
# • Add name, color, breed, legs, age to the dog dictionary
# • Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
#     • Get the length of the student dictionary
# • Get the value of skills and check the data type, it should be a list
# • Modify the skills values by adding one or two skills
# • Get the dictionary keys as a list
# • Get the dictionary values as a list

#empty dictionary
dog = {}

#adding key value pairs
dog = {'name':'Lucky', 'color':'white', 'breed':'Beagle', 'legs':'4', 'age':'5'}

#student dictionary
student = {'first_name':'Priyanka', 'last_name': 'JP', 'gender':'female', 'age': '21', 'marital_status':'single',
           'skills':['pharma'], 'country': 'India', 'city':'Hyderabad', 'address':'12453'}

#length of student dictionary
print(f"The length of student dictionay: {len(student)}")

#getting value of skills and checking datatype
print(type(student['skills']))

#modifying skills
student['skills'].extend(['singing', 'dancing'])
print(student['skills'])

#printing keys and values
print(f"The keys of student dictionary:{student.keys()}")
print(f"The values of student dictionary: {student.values()}")




