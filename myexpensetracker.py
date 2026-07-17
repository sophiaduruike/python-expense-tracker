commodity_list = [ ]
commodity_prices = [ ]
total_amount_spent = 0
commodity_name = input("Enter name of commodity bought, and enter 'done' to signify the end of commodities: ")

while commodity_name != "done":
    commodity_amount = int(input("Enter price of commodity: "))
    commodity_list.append(commodity_name)
    commodity_prices.append(commodity_amount)
    total_amount_spent += commodity_amount
    commodity_name = input("Enter name of commodity bought, and enter 'done' to signify the end of commodities: ")

for index in range(len(commodity_list)):
    print(f"you have spent {commodity_prices[index]} on {commodity_list[index]}")

print("====EXPENSE REPORT====")
print(f"List of itrms bought: {commodity_list}")
print(f"List of  amounts spent: {commodity_prices}")
print(f"Total amount spent: {total_amount_spent}")


