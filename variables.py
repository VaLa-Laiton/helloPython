# In Python, as in other languages, there are many functions specific to the language. For example: print() and type(), which I used in hello.py
# Python has reserved keywords, which have a special meaning within the language, so they cannot be used. Additionally, among these keywords, we also find methods, which are identified by having two underscores on each side (such as __init__, __add__, etc.)

# In Python, variables are declared by directly assigning them a value, and these variables act as containers that store specific data.
# Information about me:

first_name = "Angel David"
last_name = "Vargas Laiton"
country = "Colombia"
city = "Bogota"
address = "123 Main Street"
age = 19
is_married = False
skills = ["Python", "SQL", "JavaScript"]
personal_info = {
    "first_name": "Angel David",
    "last_name": "Vargas Laiton",
    "country": "Colombia",
    "city": "Bogota",
}

# The second way to declare variables in Python is to do it in a single line, as follows:

first_name2, last_name2, country2, city2, age2, is_married2 = 'Angel David', 'Vargas Laiton', 'Colombia', 'Bogota', 19, False

# Printing the values stored in the variables

print(first_name)
print(last_name)
print(country)
print(city)
print(address)
print(age)
print(is_married)
print(skills)
print(personal_info)

print('Printing the values of variables declared in the second way')
print(first_name2)
print(last_name2)
print(country2)
print(age2)
print(is_married2)