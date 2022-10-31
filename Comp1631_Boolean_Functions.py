w = 10
x = 5
y = 3
z = 8



print("1st question")
print(x == 5 and y < 3) 
print((x == 5 and y < 3) or (w != 0 and z < 10) )
print(z > 5 or (w <= 10 and x > 5))
print((y == 3 or not (w > 10)) and (not (x < 10) or (z != 5)))



x = True
y = False
z = True


print("2nd question")
print(x and y or x and z)
print((x or not y) and (not x or z))
print(x or y and z)
print(not (x or y) and z)
print(not (z or y) or x)
print(y and x and z)
print(not z or (y or not x))


"""
parenthesis take precedence 
logical complements ( not ) are performed first, 
logical conjunctions ( and ) are performed next, 
and logical disjunctions ( or ) are performed at the end. 

"""