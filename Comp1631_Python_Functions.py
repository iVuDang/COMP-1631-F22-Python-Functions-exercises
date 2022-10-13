''' 
Purpose: 
 * My solution attempts to exercises for COMP 1631-002 F22 - Functions exercises. 

Citations:
 * Problems provided by prof. Patrick Perri, Mount Royal University.  
'''

# Input , processing, and output - 8 problems
'''
1/8. Sales Prediction
A company has determined that its annual profit is typically 23 percent of total sales. 
Write a program that asks the user to enter the projected amount of total sales, then displays the profit that will be made from that amount.
'''

def findProfit(totalSales):
  annualProfit = 0.23 * totalSales
  annualProfitStr = f'Estimated profit is ${annualProfit}'
  print(annualProfitStr)

def main():

  theTotalSales = float(input("Enter totals sales:")) #use the'' in front to indicate final variable
  findProfit(theTotalSales)

main()



'''
2/8. Land Calculation
One acre of land is equivalent to 43,560 square feet. 
Write a program that asks the user to enter the total square feet 
in a tract of land and calculates the number of acres in the tract.
'''

def calcAcres(squareFeet):
    ACRES = 43560
    sqftInAcres = squareFeet / ACRES
    acresStr = f'The number of acres in the tract are {sqftInAcres}'

    print(acresStr)


def main():
    theSqftInAcres = float(
        input("Enter the total square feet of the tract of land:"))

    calcAcres(theSqftInAcres)

main()



'''
3/8. Total Purchase
A customer in a store is purchasing five items. Write a program that asks for the price of each item, 

then displays the subtotal of the sale, 
the amount of sales tax, 
and the total. 

Assume the sales tax is 5 percent.

'''

# PART A - function to perform desired output
def totalPurchase(price1, price2, price3, price4, price5):
  TAX = 0.05

  subTotal = price1 + price2 + price3 + price4 + price5
  salesTax = subTotal * TAX
  totalWithTax = subTotal * (1 + TAX)

  receiptStr = f' Subtotal: ${subTotal}\n Sales tax: ${salesTax}\n Total with taxes: ${totalWithTax}'

  print(receiptStr)

# PART B - main function to take input from user, and call prev function

def main():
  thePrice1 = float(input("Price of first item?:"))
  thePrice2 = float(input("Price of second item?:"))
  thePrice3 = float(input("Price of third item?:")) 
  thePrice4 = float(input("Price of fourth item?:"))
  thePrice5 = float(input("Price of fifth item?:"))

  totalPurchase(thePrice1, thePrice2, thePrice3, thePrice4, thePrice5)             
main()


'''
4/8 Distance Traveled

Assuming there are no accidents or delays, the distance that a car travels down the highway can be calculated with the following formula:

distance = speed x time 

A car is traveling at 110 km per hour. 

Write a program that prompts the user for the total trip time, then displays the distance travelled.
'''


# PART A

def findDistance(minutes):
  VELOCITY = 110 #km / hr

  hours = minutes/60
  distance = hours * VELOCITY

  distanceStr = f'Distance traveled: {distance} km'

  print(distanceStr)

# PART B

def main():

  theTripTime = float(input("Enter trip time in minutes:"))
  findDistance(theTripTime)


main()



'''
5/8 Sales Tax

Write a program that will ask the user to enter the amount of a purchase. The program should then compute the sales tax for a US state. 

Assume the state sales tax is 5 percent and 
the county sales tax is 2.5 percent. 

The program should display the 

amount of the purchase, 
the state sales tax, 
the county sales tax, 
the total sales tax, and 
the total of the sale (which is the sum of the amount of purchase plus the total sales tax).

'''

# PART 1
def findSalesTaxes(amount):
  STATERATE = 0.05
  COUNTYRATE = 0.025

  stateTax = STATERATE * amount
  countyTax = COUNTYRATE  * amount
  totalTax = stateTax + countyTax
  totalSale = amount + totalTax

  saleReceipt = f'Your receipt: \n State tax: {stateTax}\n County tax: {countyTax}\n Total taxes: {totalTax}\n Total sale: ${totalSale}'

  print(saleReceipt)

# PART 2
def main():
  
  thePurchaseAmount = float(input("Enter the purchase amount:"))
  findSalesTaxes(thePurchaseAmount)


main()



'''
6/8 Celsius to Fahrenheit Temperature Converter

Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:
 
Fahrenheit = (9/5)C + 32

The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit. 

'''

# PART A

def findFH(celcius):
  fraction = (9/5) * celcius 

  temperatureFH = fraction + 32

  temperatureStr = f'Temperature in Fahrenheit: {temperatureFH}'

  print(temperatureStr)

# PART B
def main():

  theCelcius = float(input("Enter temperature in Celcius:"))

  findFH(theCelcius)

main()



'''
7/8 Ingredient  Adjuster

A cookie recipe calls for the following ingredients:
•  1.5 cups of sugar
•  1 cup of butter
•  2.75 cups of flour

The recipe produces 48 cookies with this amount of the ingredients. 

Write a program that asks the user how many cookies he or she wants to make, then displays the number of cups of each ingredient needed for the specified number of cookies.

'''

# PART 1
def findIngredients(cookies):
  SUGAR = 48/1.5 #cups
  BUTTER = 48/1 #cups
  FLOUR = 48/2.75 #cups

  sugarNeeded = cookies/SUGAR
  butterNeeded = cookies/BUTTER
  flourNeeded = cookies/FLOUR

  recipeStr = f'Sugar: {sugarNeeded:.2f} cups\nButter: {butterNeeded:.2f} cups\nFlour: {flourNeeded:.2f} cups'

  print(recipeStr)

  
# PART 2 
def main():
  theCookies = int(input("Enter how many cookies:"))
  findIngredients(theCookies)


main()



'''
8/8  Stock Transaction Program

Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:
•  The number of shares that Joe purchased was 2,000.
•  When Joe purchased the stock, he paid $40.00 per share.
•  Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid for the stock.

Two weeks later, Joe sold the stock. Here are the details of the sale:
•  The number of shares that Joe sold was 2,000.
•  He sold the stock for $42.75 per share.
•  He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.

Write a program that displays the following information:
•  Joe's profit or loss
•  The total amount of commission paid to the broker

Extra challenge: Change your program so that it is re-usable and prompts the user for:
•  Number of shares
•  Initial stock price
•  Stock sale price

'''

# PART 1
def stockProfit(shares, buyPrice, salePrice):
  COMM = 0.03

  sharesBought = shares * buyPrice
  sharesSold = shares * salePrice
  commPaid = (COMM * sharesBought) + (COMM * sharesSold)
  
  net = sharesSold - (sharesBought + commPaid)

  netStr = f'Profit/Loss: ${net}\nCommission paid: ${commPaid:.2f}'

  print(netStr)


# PART 2
def main():
  theShares = int(input("Shares bought and sold: "))
  theBuyPrice = float(input("Share price when bought: "))
  theSalePrice = float(input("Share price upon sale: "))

  stockProfit(theShares, theBuyPrice, theSalePrice)

main()



#------------------------------------------------------------------------------------------------------------------------------------
# Functions - 7 problems

'''
1/8 Property Tax

A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual value. 

For example, if an acre of land is valued at $10,000, its assess-ment value is $6,000. 

The property tax is then 72¢ for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $43.20.

Write a program that asks for 

the actual value of a piece of property 
and displays the assessment value 
and property tax.

'''

# PART 1
def findPropTax(propValue):
  ASSRATE = 0.60

  assValue = ASSRATE * propValue
  taxPerValue = assValue // 100
  propTax = taxPerValue * 0.72

  valStr = f'Actual value: ${propValue:,.2f}\nAssessment value: ${assValue:,.2f}\nProperty tax: ${propTax:.2f}'

  print(valStr)

# PART 2
def main():
  thePropValue = float(input("Enter the property value:"))
  findPropTax(thePropValue)

main()



'''
2/8 Stadium Seating

There are three seating categories at a stadium. 

Class A seats cost $20, 
Class B seats cost $15, and 
Class C seats cost $10. 

Write a program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales.
'''

# PART 1
def findIncome(ticketsA, ticketsB, ticketsC):
  CLASSA = 20
  CLASSB = 15
  CLASSC = 10

  incomeA = ticketsA * CLASSA
  incomeB = ticketsB * CLASSB
  incomeC = ticketsC * CLASSC
  incomeABC = incomeA + incomeB + incomeC
  
  incomeStr = f'Income from sales = {incomeABC}'

  print(incomeStr)
  
# PART 2
def main():
  theTicketsA = int(input("Enter class A tickets: "))
  theTicketsB = int(input("Enter class B tickets: "))
  theTicketsC = int(input("Enter class C tickets: "))

  findIncome(theTicketsA, theTicketsB, theTicketsC)

main()



''' 
3/8 Paint Job Estimator

A painting company has determined that 
for every 112 square feet of wall space, 
one gallon of paint and 
eight hours of labor will be required. 
The company charges $35.00 per hour for labor. 

Write a program that asks the user to enter the square feet of wall space to be painted and 
the price of the paint per gallon. 

The program should display the following data:
•  The number of gallons of paint required
•  The hours of labor required
•  The cost of the paint
•  The labor charges
•  The total cost of the paint job

'''


# PART 1
def costJob(squareFeet, pricePaintPerGallon):
  HOURRATE = 35 # $ per hour
  PAINT = 1/112 # gallon per square feet 
  LABOR = 8/112 # hours per square feet 

  gallonsPaint = PAINT * squareFeet 
  hoursLabor =  LABOR * squareFeet

  paintCost = gallonsPaint * pricePaintPerGallon
  laborCost = hoursLabor * HOURRATE
  totalCost = laborCost + paintCost

  totalCostStr = f'Number of gallons: {gallonsPaint}\nHours of labor: {hoursLabor}\nCost of paint: {paintCost}\nCost of labor: {laborCost}\nTotal cost: {totalCost}'
    
  print(totalCostStr)

# PART 2
def main():
  theSquareFeet = float(input("Enter the square feet of wall space to be painted:"))
  thePaintPrice = float(input("Enter the price of paint per gallon:"))

  costJob(theSquareFeet, thePaintPrice)

main()



'''
4/7. Total Purchase
A customer in a store is purchasing five items. Write a program that asks for the price of each item, 

then displays the subtotal of the sale, 
the amount of sales tax, 
and the total. 

Assume the sales tax is 5 percent.

'''

# PART A - function to perform desired output
def totalPurchase(price1, price2, price3, price4, price5):
  TAX = 0.05

  subTotal = price1 + price2 + price3 + price4 + price5
  salesTax = subTotal * TAX
  totalWithTax = subTotal * (1 + TAX)

  receiptStr = f' Subtotal: ${subTotal}\n Sales tax: ${salesTax}\n Total with taxes: ${totalWithTax}'

  print(receiptStr)

# PART B - main function to take input from user, and call prev function

def main():
  thePrice1 = float(input("Price of first item?:"))
  thePrice2 = float(input("Price of second item?:"))
  thePrice3 = float(input("Price of third item?:")) 
  thePrice4 = float(input("Price of fourth item?:"))
  thePrice5 = float(input("Price of fifth item?:"))

  totalPurchase(thePrice1, thePrice2, thePrice3, thePrice4, thePrice5)             
main()


'''
5/7. Feet to Inches

One foot equals 12 inches. 

Write a function named feet_to_inches that accepts a number of feet as an argument and returns the number of inches in that many feet. 

Use the function in a program that prompts the user to enter a number of feet then displays the number of inches in that many feet.
'''

# PART A - The function for an output
def feet_to_inches(ft):
  INCHESPERFEET = 12

  feet = ft * INCHESPERFEET

  print(feet)


# PART B - main function to take input and call on previous functions 
def main():
  theFeet = float(input("Enter number of feet:"))

  feet_to_inches(theFeet)


main()



'''
6/7. Falling Distance

When an object is falling because of gravity, the following formula can be used to determine the distance the object falls in a specific time period:

 distance = (1/2) * (g)(t)**2 

The variables in the formula are as follows: 
d is the distance in meters, 
g is 9.8, and 
t is the amount of time, in seconds, that the object has been falling.

Write a function named falling_distance that accepts an object’s falling time (in seconds) as an argument. 

The function should return the distance, in meters, that the object has fallen during that time interval.

'''

# PART A - function for output

def falling_distance(seconds):
  GRAVITY = 9.8 # meters per second
  secondsSquared = seconds**2
  
  distanceMeters = (GRAVITY * secondsSquared)/2

  print(distanceMeters)


# PART B - main function to take user input and call previous functions

def main():

  theSeconds = float(input("Enter falling time in seconds:"))

  falling_distance(theSeconds)


main()



'''
7/7. Future Value

Suppose you have a certain amount of money in a savings account that earns compound monthly interest, and you want to calculate the amount that you will have after a specific number of months. The formula is as follows:

F = P * (1 + i)**t

The terms in the formula are:
•  F is the future value of the account after the specified time period.
•  P is the present value of the account.
•  i is the monthly interest rate.
•  t is the number of months.

Write a program that prompts the user to enter the account’s present value, monthly interest rate, and the number of months that the money will be left in the account. 

The program should pass these values to a function that returns the future value of the account, after the specified number of months. 

The program should display the account’s future value.
'''


# PART 1 - function to output
def calcFV(PV, Rate, Nper):
  rateOne = (1 + Rate)
  rateSquareN = rateOne ** Nper

  fvCalc = PV * rateSquareN

  print(fvCalc)

# PART 2 - main function to take user input and 
def main():
  thePV = float(input("Enter the account's present value:"))
  theRate = float(input("Enter the monthly interest rate:"))
  theNper = float(input("Enter number of months the money will stay in the account:"))

  calcFV(thePV, theRate, theNper)


main()

  




