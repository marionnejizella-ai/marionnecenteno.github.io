#Exercise 3: Biography
#Marionne Jizella E. Centeno

name = input("Marionne Jizella E. Centeno: ")
age = input("18: ")
hometown = input("Philippines: ")

try: 
    age = int(age_input)
except ValueError:
    print("Invalid age. Setting age to 0.")
    age = 0


person = {
    "name": 'Marionne Jizella E. Centeno',
    "age": '18',
    "hometown": 'Philippines'
}

print("\n--- Biography ---")
print("Name:", person ["name"])
print("Age:", person ["age"])
print("Hometown:", person ["hometown"])