def input_integer(prompt):
    while True:
        try:
            # Converts the input to integer 
            user_input = int(input(prompt))

            # Checking for positive integer only
            if user_input >= 0:
                return user_input
            else:
                print("Positive integer only! \n")
        except ValueError:
            print("Valid number only! \n")

def yes_or_no(prompt):
    while True:
        # Converting the input to lowercase for case-insensitivity
        answer = input(prompt).lower()

        # Check if the entered value is 'y' or 'n'
        if answer in ['y', 'n']:
            return answer
        else:
            print("Answer 'Y' or 'N' only. \n")

def pizza_price(number_of_pizzas, delivery_required, is_tuesday, app_usage):
    price_per_pizza = 12
    delivery_charge = 2.50
    tuesday_discount = 0.5
    app_discount = 0.25

    # Calculate the base price
    final_price = number_of_pizzas * price_per_pizza

    # Add delivery charge where it is free if the order is 5 or above
    if delivery_required.lower() == 'y'and number_of_pizzas <= 5 :
        final_price += delivery_charge

    # Apply Tuesday discount if it's Tuesday
    if is_tuesday.lower() == 'y':
        final_price *= (1-tuesday_discount)

    # Apply app discount if the app was used
    if app_usage.lower() == 'y':
        final_price *= (1-app_discount)

    # To return 2 digits after decimal point 
    final_price = "{:.2f}".format(final_price) 
    return final_price

try:
    print("\nBIG MAN'S PIZZERIA")
    print("========================== \n")

    number_of_pizzas = input_integer("How many pizzas for your order? ")
    
    delivery_required = yes_or_no("Is delivery needed for the pizzas? (Y/N) ")

    is_tuesday = yes_or_no("Is today Tuesday? (Y/N) ")
    
    app_usage = yes_or_no("Have you connected us via our app? (Y/N) ")

    final_price = pizza_price(number_of_pizzas, delivery_required, is_tuesday, app_usage)

    # Final output displaying everything
    print(f"\nTotal Price: £{final_price}\n")

except ValueError:
    print("Error! Try again with a vaild input")

print("Here's your price breakdown") 
print("=========================== \n")
print(f"Your total ordered pizza is {number_of_pizzas} \n")
    
if delivery_required == 'y':
    print("Extra £2.50 was charged for the delivery! \n")
else:
    print("We don't add delivery charges on 5 or more pizza orders anyway :) \n")

if is_tuesday == 'y':
    print("50% off on all pizzas on Tuesday except in delivery charges. \n")
else:
    print("On Tuesdays, there’s a 50% discount on the total price, excluding delivery charges! \n")

if app_usage == 'y':  
    print("25% discount for ordering via our app. \n")
else:
    print("You'll get 25% discount on all price had you ordered via our app! \n")