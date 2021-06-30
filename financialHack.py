credit = float(input("Please enter the amount of currency you receive on your credit card each week: $"))
cash = float(input("Please enter the amount of currency you receive in physical form each week: $"))
savings = float(input("Please enter the amount of money you plan to save each week in case of emergencies: $"))
credit -= savings
waterCost = float(input("Please enter the price of an individual bottle of water from your local store: $"))
water = int(input("Please enter the amount of bottles of water you plan to purchase this week: $"))
waterPrice = water * waterCost
cash -= waterPrice
sodaCost = float(input("Please enter the price of an individual bottle of soda from your local store: $"))
soda = int(input("Please enter the amount of individual bottles of soda you plan to purchase this week: $"))
sodaPrice = soda * sodaCost
cash -= sodaPrice
bathroomCost = float(input("Please enter the amount of money you have spent on your bathroom necessities this week: $"))
credit -= bathroomCost
fastfoodCost = float(input("Please enter the amount of money you spend at your local fast food restaurant each week: $"))
credit -= bathroomCost
print("Money you have left at the end of the week on hand for other expenses: " + cash)
print("Money you have left at the end of the week on your credit card for other expenses: " + credit)
