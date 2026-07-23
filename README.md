# Expense Tracker
A command line python program that tracks purchase and calculates total spending.

## What it does
-Prompts the user to enter names of commodities bought and their amounts, i.e., expense names and amounts, one at a time
-Type "done" to finish entering expenses
-Stores each expense name in a list
-Stores each expense amount in another list
-Prints a summary report showing every item, amount, and the total spent
-Prompts the user to enter the category of each commodity bought
-Stores the different categories in a list
-Stores the amounts spent on each category in a dictionary using the category names as the keys and the amounts spent on that category as the value
-Calculates and prints the average amount of money spent on each commodity

## What I learned
-Using a priming read with a while loop
-Debugging an accumulator bug caused by an unused index variable - the total was double-counting an early entry instead of adding up all entries correctly
-Breaking code into functions to organize related tasks
-Using the global keyword to modify variables from outside a function's local scope
-Using Dictionaries to group and total values by category
-Refactored a working V1 into V2 by rebuilding the same features with new tools

## Tech
Python - loops, lists, conditionals, string formatting(f-strings), functions, dictionaries, global scope.