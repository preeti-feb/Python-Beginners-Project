print("`" * 50)
print("Expense Tracker")
print("`" * 50)


user_name = input("\nEnter your name: ")
initial_balance = int(input("\nEnter your initial balance: "))
expenses_list = []
expenses_number = int(input("How many expenses do you want to enter? - "))


for expenses in range(expenses_number):
    expenses_amount = int(input("Enter the expense amount: "))
    expenses_list.append(expenses_amount)


total_expenses = sum(expenses_list)
remaining_balance = initial_balance - total_expenses


if remaining_balance > 0:
    financial_status = ("Within Budget")
elif remaining_balance == 0:
    financial_status = ("Budget fully used")
else:
    financial_status = ("Over Budget")



print("\n-" * 40)
print("Your Financial Report based on your all expenses")
print("-" * 40)

print(f"\nName: {user_name}")
print(f"Your initial balance = {initial_balance}")
print(f"Your total expenses balance = {total_expenses}")
print(f"Your remaining balance = {remaining_balance}")
print(f"Your Financial status: {financial_status}")

print("\nTake your financial life seriously and do expenses necessary only.")
