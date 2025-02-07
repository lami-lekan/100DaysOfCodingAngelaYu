print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10,12, or 15? "))
num_of_customers = int(input("How many people to split the bill?"))

total_cost = total_bill * (1 + (tip_percent/100))
each_bill = total_cost / num_of_customers

print(f"Each person should pay ${round(each_bill, 2)}")