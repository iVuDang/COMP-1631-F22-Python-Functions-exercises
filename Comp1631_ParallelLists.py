
# PARALLEL LISTS - Find oldest person, with list of names, and list of ages. 

ages = [19,18,20]
names = ["Aaliya", 'Farah', 'Sada']

oldest_age = max(ages)
position_oldest_names = ages.index(oldest_age)

oldest_name = names[position_oldest_names] # List[index position in the list]


print(oldest_name)
# Sada



print ("--------------------")
#-------------------------------------------------------------------------------



"""
Parallel Lists:
* Each list is the same length
* Each list maintains the original order (keeps association)
"""

number = [3, 65, 77]
street = ["Richard Road", "Richmond Road", "Radcliffe Bay"]
quadrant = ["SW", "SW", "SE"]

address = []  # empty accumulator list
i = 0  # iterations accumulator AND to index sequence

while i < len(number):
  address.append(f'{number[i]} {street[i]} {quadrant[i]}')
  i += 1

print(address)
# ['3 Richard Road SW', '65 Richmond Road SW', '77 Radcliffe Bay SE']