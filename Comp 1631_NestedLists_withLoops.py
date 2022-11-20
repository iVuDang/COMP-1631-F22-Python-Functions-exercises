gods = [['Odin', 'Frigg', 'Thor', 'Tyr'],
        ['Kihci Manito', 'Grandmother Fox', 'Ayas', 'Pithisiw'],
        ['An', 'Nammu', 'Enki', 'Ereshkigal']]

# Print the item that is 'Enki'
print(gods[2][2])
#Enki


#-------------------------------------------------------------------------------


# Create a new list of just the first column, using a loop.
column_accum = []
z = 0

while z < len(gods):
  column_value = gods[z][0]
  column_accum.append(column_value)
  z += 1
  
print(column_accum)
#['Odin', 'Kihci Manito', 'An']


#-------------------------------------------------------------------------------


# Print row 1, as a list
print(gods[0])
# ['Odin', 'Frigg', 'Thor', 'Tyr']

# Print row 3’s items, one at a time
for a in gods[2]:
  print(a)
"""
An
Nammu
Enki
Ereshkigal
"""


#-------------------------------------------------------------------------------


# Create a new list of just row, using a loop
for x in gods:
  i = 0

  while i < len(x):
    print(x[i])
    i = i + 1
"""
Odin
Frigg
Thor
Tyr
Kihci Manito
Grandmother Fox
Ayas
Pithisiw
An
Nammu
Enki
Ereshkigal
 
"""
