from datetime import datetime

print("-" * 40)
print("-" * 40)
print("DIGITAL TIME CAPSULE")
print("-" * 40)
print("-" * 40)

print("\nWelcome to your personal time capsule.")
print("Create a life that you deserve from yourself. ~ PREETI KUMARI")

name = input("\nEnter your name: ")
future_message = input("Enter your message for your future self: ")

print("\nWhen do you want to open your time capsule?")
unlock_date = input("Enter unlocking date (DD-MM-YYYY): ")

creation_date = datetime.now().strftime("%d-%m-%Y")

is_valid = False

try:
    valid_date = datetime.strptime(unlock_date, "%d-%m-%Y")
    is_valid = True
    print("\nValid date!")

except ValueError:
    print("\nInvalid date! Please enter DD-MM-YYYY.")

if is_valid:
    with open("time_capsule.txt", "w") as file:
        file.write("DIGITAL TIME CAPSULE\n")
        file.write("-" * 30 + "\n")
        file.write(f"Name: {name}\n")
        file.write(f"Created On: {creation_date}\n")
        file.write(f"Message: {future_message}\n")
        file.write(f"Unlock Date: {unlock_date}\n")

    print("\nYour time capsule has been saved successfully!")

else:
    print("\nYour time capsule was not saved.")
