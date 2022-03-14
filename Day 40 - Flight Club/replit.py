import requests

SHEETY_POST = "https://api.sheety.co/4e9a0b7202595531f9878e402cb95989/flightDeals/users"

print("Welcome to Vitaliy's Fight Club!")
print("We find the best flight deals and email you.")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email1 = input("What is your email?\n")
email2 = input("Type your email again.\n")
if email1 == email2:
    print("You're in the club!")

parameters = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email1,
}
}

response = requests.post(url=SHEETY_POST, json=parameters)
data = response.json()
print(data)