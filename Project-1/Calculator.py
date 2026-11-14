def calculator():
    print("*"*35)
    print("Simple Calculator")
    print("*"*35)
    print("\n1- Addition")
    print("2- Subtraction")
    print("3- Multiplication")
    print("4- Division")

    choice = input("\nEnter your choice to make mathematical operations (1-4): ")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))


    if choice == "1":
        print(f"The addition of {num1} and {num2} is {num1 + num2}")
    
    elif choice == "2":
        print(f"The subtraction of {num1} and {num2} is {num1 - num2}")

    elif choice == "3":
        print(f"The multiplication of {num1} and {num2} is {num1 * num2}")
       
    elif choice == "4":
        if num2 == 0:
            print("Error! Cannot divide by zero.")
        else:
            print(f"The Division of {num1} and {num2} is {num1 / num2}")

    else:
        print("Invalid choice!")


calculator()
