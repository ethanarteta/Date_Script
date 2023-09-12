# Date Night Budget Planner

# Welcome message and program description
print("Welcome to date night")

# Prompt for the name of the date partner
date_name = input("Who are you going on a date with? ")

# Prompt for the budget and convert it to a float
budget = float(input("What is your budget? "))
new_budget = budget  # Create a variable to track remaining budget

# Define the menu with item names and prices
menu = {"appetizer": 10.00, "entree": 25.00, "dessert": 8.00, "drink": 5.00}

# Initialize total expenses
total_expenses = 0.00

# Start a loop to select menu items while the budget is available
while new_budget > 0.00:
    print("\nMenu:")
    # Display the menu items and prices
    for item, price in menu.items():
        print(f"{item.capitalize()}: ${price}")
    
    # Prompt for the choice of menu item or 'done' to finish ordering
    choice = input("\nWhat do you want to eat and drink? (or 'done' to finish ordering): ").lower()

    # Check if the user wants to finish ordering
    if choice == 'done':
        break

    # Check if the choice is a valid menu item
    if choice in menu:
        expense = menu[choice]
        # Check if the budget allows for the selected item
        if new_budget >= expense:
            total_expenses += expense
            new_budget -= expense
            print(f"Ordered {choice.capitalize()}. Remaining budget: ${new_budget:.2f}")
        else:
            print("You don't have enough budget for that choice.")
    else:
        print("Invalid choice. Please choose from the menu options.")

# Check if total expenses exceed the initial budget
if total_expenses > budget:
    print("\nSorry, it seems you overspent. No second date.")
else:
    print(f"\nGreat job! You have ${new_budget:.2f} left. There may be a second date with {date_name}!")
