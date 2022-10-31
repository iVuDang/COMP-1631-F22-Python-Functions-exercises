# Practice problems provided by Comp 1631 - Mount Royal University - Prof. Patrick Perri

"""
4. Write a Python function that takes 3 integers representing dice rolls as inputs. If all 3 are the same value, return "3 of a kind!". 

If 2 are the same, return "a pair!". 
Otherwise, return "Roll again """


def check_Pair (dice1, dice2, dice3):

  d1d2d3_agreed = (dice1 == dice2 == dice3)
  d1d2_agreed = (dice1 == dice2)
  d2d3_agreed = (dice2 == dice3)
  d1d3_agreed = (dice1 == dice3)
  
  
  if d1d2d3_agreed:
    return "3 of a kind!"
  elif (d1d2_agreed or d2d3_agreed or d1d3_agreed):
    return "a pair!"
  else:
    return "Roll again"


print(check_Pair(3,3,3))
print(check_Pair(3,3,1))
print(check_Pair(1,2,3))


'''
5. following tax structure:
Tax rate	   No dependents	            Dependents
0%	        Less than  $20,000	       Less than $40,000
10%	        $20,000 to $60,000	       $40,000 to $60,000
20%        	$60,000 and over	          $60,000 and over

Write an algorithm that asks how many dependents the user has and 
how much money they made, 

then prints out the amount of tax owing. How would you test whether this program is working correctly?

'''

tax_rate = 0

def tax_nodependents(income):
  if (income < 20000):
    tax_rate = 0
  elif ((income >= 20000) and (income < 60000)):
    tax_rate = 0.1
  else:
    tax_rate = 0.2 

  tax_calc = tax_rate * income
  return tax_calc 

print(tax_nodependents(60000))
    

def tax_dependents(income):
  if (income < 40000):
    tax_rate = 0
  elif ((income >= 40000) and (income < 60000)):
    tax_rate = 0.1
  else:
    tax_rate = 0.2 

  tax_calc = tax_rate * income
  return tax_calc 

print(tax_dependents(40000))

  

def main_tax_calc(dependents,income):
  the_tax_value = 0
  
  if (dependents == 0):
    the_tax_value = tax_dependents(income)
  elif (dependents > 0):
    the_tax_value = tax_nodependents(income)
  else:
    "Need to enter dependents and income 0 or greater"

  return the_tax_value

print(main_tax_calc(0,60000))
print(main_tax_calc(1,40000))
print(main_tax_calc(0,0))



'''
6. Design an algorithm for the following problem: The GPA of a student is entered via the keyboard. A message is printed that is dependent on the value of the GPA as shown below.
GPA	Message

3.0 to 4.0	Keep up the great work!
2.0 to 2.9	Room for improvement, but you're getting there
1.0 to 1.9	You're falling behind, is everything okay?
0.0 to 0.9	:(

A.	If the user enters a number above 4.0 or below 0.0 display the message Invalid Input.
B.	Which test values would you use to test all possible categories?

'''

def display_gpa_message(gpa):

  message = ""

  if ((gpa >= 3.0) and (gpa < 4.0)):
    message = "Keep up the great work!"
  elif ((gpa >= 2.0) and (gpa < 2.9)):
    message = "Room for improvement, but you're getting there"
  elif ((gpa >= 1.0) and (gpa < 1.9)):
    message = "You're falling behind, is everything okay?"
  elif ((gpa == 0) and (gpa < 0.9)):
    message = ":("
  else:
    message = "Invalid input"

  return message


print(display_gpa_message(2.5))
print(display_gpa_message(3.0))
    

def sales_tax(subtotal: float, province: str) -> float:
  '''Finds the sales tax based on province-
    AB, and all of the territories= 0%, 
    BC and MN= 7%, 
    ON = 8%, 
    SK = 6%, 
    QC 9.975%, 
    all other provinces = 10%'''

  tax_calc = 0

  if (province == "AB"):
    tax_calc = 0 * subtotal
  elif (province == ("BC" or "MN")):
    tax_calc = 0.07 * subtotal
  elif (province == "ON"):
    tax_calc = 0.08 * subtotal
  elif (province == "QC"):
    tax_calc == 0.0975 * subtotal
  else:
    tax_calc = 0.1 * subtotal

  tax_calc_str = f'The sales tax is ${tax_calc:.2f}'
  print(tax_calc_str)

print(sales_tax(100, "ON"))


def main():
  the_subtotal = float(input("Enter subtotal:"))
  the_province = str(input("Enter province - AB, BC, MN, ON, SK, QC:"))

  sales_tax(the_subtotal, the_province)

main()


"""
3.	Design a program that prompts the user for the dollar amount of their current order, then prints out a message according to the following table:

Amount	Message
amount <0	          Invalid entry, orders must be positive
0≤ amount <40	      Add $xx.xx to your order to get free delivery
40 ≤ amount	        You get free delivery!
"""


def calc_remain(spend):
  remain = 40 - spend
  remain_str = f'Add ${remain:.2f} to your order to get free delivery'

  print(remain_str)


print(calc_remain(25.30))


def check_free_delivery(amount):
  message = ""

  if (amount < 0):
    message = "Invalid entry, orders must be positive"
  elif (amount >= 0 and amount < 40):
    message = calc_remain(amount)
  elif (amount >= 40):
    message = "You get free delivery"
  else:
    message = "Recheck inputs"

  print(message)

print(check_free_delivery(25.30))


def main():
  the_amount = float(input("Enter your order amount:"))

  check_free_delivery(the_amount)

main()