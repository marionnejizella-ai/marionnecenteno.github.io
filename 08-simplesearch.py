#Exercise 8: Simple Search
#Marionne Jizella E. Centeno

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_term = input("Enter the name you are looking for:")
if search_term.strip() in names:
    print(f"Yes, {search_term} was found in the list.")
else:
    print(f"Sorry, {search_term} is not on the list.")

if search_term.lower() in [name.lower() for name in names]:
    print(f"{search_term} was found in the list.")
else:
    print(f"{search_term} was  NOT found in the list.")
