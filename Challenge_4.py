# Write a script that asks for an amount of change
# (as in money you get back when paying for something in cash)
# Then tells you how many of each type of coin to use to make that amount
#   Example:
#       How much change do you need?
#       83
#       3 quarters, 0 dimes, 1 nickel, 3 pennies


changeAmount = int(input("How much change do you need?\n"))
quarters = changeAmount/25
quarters=round(quarters)
changeAmount=changeAmount%25
dimes = changeAmount/10
dimes=round(dimes)
changeAmount=changeAmount%10
nickels = changeAmount/5
nickels=round(nickels)
changeAmount=changeAmount%5
pennies = changeAmount


#your code here

print(quarters,"quarters,",dimes,"dimes,",nickels,"nickels,",pennies,"pennies")