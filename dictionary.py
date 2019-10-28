# dictionary is made by using the symbol of {} likewise sets...but they contain two components of keys and values of it
# example of the dictionary is as follows

# student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# print(student)

# student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# print(len(student))

# student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# print(student["name"])
# print(student["age"])

# student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# print(student.get("phone", "Not found"))   # agar koi aesi value likhi jae to dictionary mn na hoto by default none likha hua
                                           #ayega...but we can change the default message like i did here by not found

# student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# student["name"] = "Asim"
# student["phone"] = "03082790862"   #in this way you can add and key and value into the dictionary
# print(student)

# another method to add the key and value in dictionary the keyword of update is used

# student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# student.update({"name": "Asim", "phone": "03009217446"})
# print(student)

# to delete any key from the dictionary by using the del keyword
# student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# del student["age"]
# print(student)

# to any key can be deleted from the dictionary by using the pop out keyword...it also useful cuz we can get the return
# the value by using the pop keyword

#student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# student.pop("age")   #by using this we couldn't get the return value shat is popped out
# print(student)

# popped_value = student.pop("age")
# print(student)
# print(popped_value)

# to get the keys, values and the items in the dictionary

# student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# print(student.keys())

# print(student.values())

# print(student.items())

student = {"name": "Aaqib", "age": "18", "course": ["Maths", "Physics"]}
# for keys in student:
#      print(keys)

# for keys, values in student.items():
#     print(keys, values)