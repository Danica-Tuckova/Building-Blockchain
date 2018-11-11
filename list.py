# Create a list of person dictionaries with name, age and list of hobbies for each person

person_list = [
    {"name": "Bob", "age": 30, "hobbies": ["xds"]},
    {"name": "Alexa", "age": 24, "hobbies": ["xdd"]},
    {"name": "David", "age": 34, "hobbies": ["xdsff"]}
]

# Use a list comprehension to convert this list of person`s into a list of names (of the persons)

list_of_names = [el["name"] for el in person_list]
print(list_of_names)


# Use a list comprehension to check whether all persons are older than 20

check_age = all([el["age"] > 20 for v in person_list])
print(check_age)

# Copy the person list such that you can safety edit the name of the first person (without changing the original list)

copy_list_of_names = person_list[:]

# Unpack the persons on the original list into different variables and output these variables

print(copy_list_of_names)
print(person_list)
copy_list_of_names[0]["name"] = "MMi"
print(copy_list_of_names)
print(person_list)

        