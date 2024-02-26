#Patches56
#Data validation

user_pw= input("Enter password: ")
num_attempts = 1

while user_pw != "WCC" and num_attempts <= 3:
    user_pw= input("Invalid! Enter password: ")
    num_attempts += 1

print("Login successful")
