amount = float(input("Enter amount: ")) # Input the amount
inrate = float(input("Enter interest rate: ")) # Input the rate
period = int(input("Enter period: ")) #Input the period
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year, value))
    amount = value
    year = year + 1 