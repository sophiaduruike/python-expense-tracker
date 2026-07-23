commodity_list = [ ]
commodity_prices = [ ]
category_list = [ ]
total_amount_spent = 0
category_totals = { }

def add_expense():
    global commodity_name
    global total_amount_spent

    commodity_list.append(commodity_name)

    commodity_amount = int(input("Enter price of commodity in Naira: "))
    commodity_prices.append(commodity_amount)
    total_amount_spent += commodity_amount

    commodity_category = input("Enter category of commodity. E.g 'Food', 'Transport', 'Data' ")
    category_list.append(commodity_category)

    category_totals[commodity_category ] = category_totals.get(commodity_category, 0) + commodity_amount
    commodity_name = input("Enter name of commodity bought, and enter 'done' to signify the end of commodities: ")

def print_report():
    average_amount_per_expense = total_amount_spent / len(commodity_list)
    print("====EXPENSE REPORT====")
    print(f"List of items bought: {commodity_list}")
    print(f"List of  amounts spent: {commodity_prices}")
    print(f"Total amount spent: {total_amount_spent}")
    print(f"The average amount per expense is: {average_amount_per_expense}")
    print(f"Money spent on eachcategory {category_totals}")

commodity_name = input("Enter name of commodity bought, and enter 'done' to signify the end of commodities: ")
while commodity_name != "done":
    add_expense()

print_report()