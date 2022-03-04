#This is the simplest task for testing input skills

print(f"Welcome to the Band Name Generator.\n{'*'*35}")
street = input("What's the name of the city you grew up in?\n")
pet = input(f"What's your first pet's name?\n")
print("*"*35)
print(f"Your band name could be {street.title()} {pet.title()}")