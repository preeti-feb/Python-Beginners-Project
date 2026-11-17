print("-"* 40)
print("SECRET CODE GENERATOR")
print("-"* 40)


user_message = input("\nEnter a word to generate a secret code: ")

encrypted_message = ""

for character in user_message:
    unique_code = ord(character)
    new_value = unique_code + 3
    new_character = chr(new_value)

    encrypted_message += new_character


print(f"\nYour secret code: {encrypted_message}.")
