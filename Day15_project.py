from Day15_data import material_qty
# coffee maker
water = material_qty[0]['water']
milk = material_qty[2]['milk']
coffee = material_qty[1]['coffee']


# TODO: 1. create power on and off feature
def on_off():
    on_or_off = input("Welcome! Turn on coffee maker. Y/N: ").lower()
    if on_or_off.startswith('y'):
        return True
    else:
        return False


# TODO: 2. create display menu
def display_menu():
    print("Loading...100%")
    option = input("Pick an option:\n1. make espresso\n2. make latte\n3. make cappuccino\n4. material report\n5. "
                   "refill material\n6. Switch off: ")
    return option


# TODO: 3. create material report feature
def material_report():
    msg = f"Water = {water}\nMilk = {milk}\nCoffee = {coffee}\n"
    return msg


def coffee_process(coffee_type):
    global water, milk, coffee
    if not material_enough(coffee_type):
        return "Sorry, not enough materials to make this coffee."
    if coffee_type == 'espresso':
        water -= 50
        coffee -= 18
        return "Here is your espresso. Enjoy!"
    elif coffee_type == 'latte':
        water -= 200
        coffee -= 24
        milk -= 150
        return "Here is your Latte. Enjoy!"
    elif coffee_type == 'cappuccino':
        water -= 250
        coffee -= 24
        milk -= 100
        return "Here is your cappuccino. Enjoy!"


# TODO: 4. check if material is enough
def material_enough(coffee_type):
    """To check if there is enough material for the coffee"""
    if coffee_type == 'espresso' and water >= 50 and coffee >= 18:
        return True
    elif coffee_type == 'latte' and water >= 200 and coffee >= 24 and milk >= 150:
        return True
    elif coffee_type == 'cappuccino' and water >= 250 and coffee >= 24 and milk >= 100:
        return True
    else:
        return False


# TODO: 5. ask for coin and process payment
def coin():
    """To calculate payment"""
    print("\nInsert your money.")
    print("You can only insert 25cents; 10cents & 5cents")
    while True:
        try:
            quarter = int(input("How many $0.25: "))
            dime = int(input("How many $0.10: "))
            nickel = int(input("How many $0.05: "))

            if quarter < 0 or dime < 0 or nickel < 0:
                print("Please enter non-negative numbers.\n")
                continue
            total = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05)
            return total
        except ValueError:
            print("Invalid input! Please enter whole numbers only.\n")


# TODO: 6. make coffee if all checks out
def refill():
    global water, coffee, milk
    confirmation = input("Are you sure you want to refill all materials? (Y/N): ").lower()
    if confirmation == 'y':
        water = 1500
        milk = 1000
        coffee = 600
        print("Refill successful.")
    else:
        print("Refill cancelled")


def coffee_maker():
    run_machine = on_off()
    while run_machine:
        print("\n")
        pick = display_menu()

        if pick == '1':
            pay = coin()
            enough_mat = material_enough('espresso')
            if enough_mat:
                if pay >= 1.50:
                    print(coffee_process('espresso'))
                    if pay - 1.50 != 0:
                        print(f"And here is your change: ${pay - 1.50:.2f}\n")
                else:
                    print(f"Sorry not enough coin. You need $1.50. Your ${pay} is refunded\n")
            else:
                print("Sorry not enough material")

        elif pick == '2':
            pay = coin()
            enough_mat = material_enough('latte')
            if enough_mat:
                if pay >= 2.50:
                    print(coffee_process('latte'))
                    if pay - 2.50 != 0:
                        print(f"And here is your change: ${pay - 2.50:.2f}\n")
                else:
                    print(f"Sorry not enough coin. You need $2.50. Your ${pay} is refunded\n")
            else:
                print("Sorry not enough material")

        elif pick == '3':
            pay = coin()
            enough_mat = material_enough('cappuccino')
            if enough_mat:
                if pay >= 3.00:
                    print(coffee_process('cappuccino'))
                    if pay - 3.00 != 0:
                        print(f"And here is your change: ${pay - 3.00:.2f}\n")
                else:
                    print(f"Sorry not enough coin. You need $3.00. Your ${pay} is refunded\n")
            else:
                print("Sorry not enough material")

        elif pick == '4':
            print(material_report())
        elif pick == '5':
            refill()
        elif pick == '6':
            run_machine = False
        elif pick not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice! Please select a valid choice option.\n")


coffee_maker()
